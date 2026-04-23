from snowflake.snowpark import Session
import os
from dotenv import load_dotenv

load_dotenv()

def run_transformations():
    # 1. Connect to Snowflake
    connection_parameters = {
        "account": os.getenv('SNOW_ACCOUNT'),
        "user": os.getenv('SNOW_USER'),
        "password": os.getenv('SNOW_PASS'),
        "role": "ACCOUNTADMIN",
        "warehouse": os.getenv('SNOW_WH'),
        "database": os.getenv('SNOW_DB'),
        "schema": os.getenv('SNOW_SCHEMA')
    }
    
    session = Session.builder.configs(connection_parameters).create()

    # 2. Load data from S3 Stage into Snowflake Table
    session.sql("COPY INTO RAW_SALES FROM @my_s3_stage/raw_data/ FILE_FORMAT = (TYPE = CSV SKIP_HEADER = 1)").collect()
    
    # 3. Transformation: Filter high-value sales (Silver Layer)
    df_raw = session.table("RAW_SALES")
    df_cleaned = df_raw.filter(df_raw["amount"] > 100)
    
    # 4. Save to a new 'Silver' table
    df_cleaned.write.mode("overwrite").save_as_table("CLEAN_HIGH_VALUE_SALES")
    
    print("✅ Success: Snowflake transformation complete!")
    session.close()

if __name__ == "__main__":
    run_transformations()
