❄️ End-to-End Cloud Data Pipeline: AWS & Snowflake

📌 Project Overview
This project is a automated data pipeline that extracts raw data from an external source, stores it in AWS S3, and then loads and transforms it within Snowflake using Python (Snowpark). It follows the Medallion Architecture (Raw -> Clean -> Analytics).

🛠️ Technology Stack
Language: Python 3.9+
Cloud Storage: AWS S3 (Data Lake)
Data Warehouse: Snowflake (Cloud Data Cloud)
Transformation: Snowpark (Python API for Snowflake
Orchestration: Python Scripts

🏗️ Architecture
Ingestion: Python script fetches data (e.g., Daily Weather or Stock Prices) and uploads it to an AWS S3 Bucket.
Staging: Snowflake connects to the S3 bucket using an External Stage.
Loading: Data is moved from the S3 stage into a "Bronze" (Raw) table.
Transformation: A Snowpark script cleans the data, handles nulls, and saves it to a "Silver" (Cleaned) table for analysis.
