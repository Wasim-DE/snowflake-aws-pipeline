-- Create Database and Schema
CREATE OR REPLACE DATABASE DEMO_DB;
CREATE OR REPLACE SCHEMA DEMO_DB.PUBLIC;

-- Create a Warehouse for compute
CREATE OR REPLACE WAREHOUSE COMPUTE_WH WITH WAREHOUSE_SIZE = 'XSMALL' AUTO_SUSPEND = 60;

-- Create a Table for Raw Data (Bronze Layer)
CREATE OR REPLACE TABLE DEMO_DB.PUBLIC.RAW_SALES (
    transaction_id STRING,
    customer_id STRING,
    product STRING,
    amount NUMBER,
    sale_date DATE
);

-- Create an External Stage (Points to S3)
-- Replace with your bucket URL
CREATE OR REPLACE STAGE my_s3_stage
  URL = 's3://your-bucket-name/'
  CREDENTIALS = (AWS_KEY_ID = 'your_key' AWS_SECRET_KEY = 'your_secret');
