import boto3
import pandas as pd
from io import StringIO
import os
from dotenv import load_dotenv

load_dotenv()

def upload_to_s3():
    # 1. Create Dummy Data
    data = {
        'transaction_id': ['T101', 'T102', 'T103'],
        'customer_id': ['C1', 'C2', 'C3'],
        'product': ['Laptop', 'Mouse', 'Monitor'],
        'amount': [1200, 25, 300],
        'sale_date': ['2023-10-01', '2023-10-02', '2023-10-03']
    }
    df = pd.DataFrame(data)
    
    # 2. Convert to CSV in memory
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)

    # 3. Upload to S3
    s3 = boto3.resource('s3', 
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
        aws_secret_access_key=os.getenv('AWS_SECRET_KEY')
    )
    
    s3.Object(os.getenv('S3_BUCKET_NAME'), 'raw_data/sales.csv').put(Body=csv_buffer.getvalue())
    print("✅ Success: Data uploaded to S3!")

if __name__ == "__main__":
    upload_to_s3()
