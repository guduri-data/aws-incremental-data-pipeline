# AWS Incremental Batch Data Pipeline (Project 2)

This project demonstrates an incremental batch data pipeline built using AWS S3 and AWS Glue, where only new data partitions are processed on each run using a date-based ingestion strategy.

Problem Statement  
In real-world data engineering systems, reprocessing the entire dataset every day is inefficient and costly. This project solves that problem by processing only newly arrived data using date-based S3 partitions.

Architecture  
S3 Raw (CSV, partitioned by ingest_date) → AWS Glue (Parameterized PySpark Job) → S3 Silver (Parquet, partitioned by ingest_date)

S3 Folder Structure  

Raw Layer  
s3://surya-project2/raw/orders/  
ingest_date=2026-01-01/orders.csv  
ingest_date=2026-01-02/orders.csv  

Silver Layer  
s3://surya-project2/silver/orders/  
ingest_date=2026-01-01/  
ingest_date=2026-01-02/  

AWS Glue Job  
The AWS Glue job is parameterized using --ingest_date. Each job run processes only one partition based on the provided date. Running the same job multiple times with different dates enables incremental processing without reprocessing historical data.

Example Job Runs  
--ingest_date=2026-01-01  
--ingest_date=2026-01-02  

Key Features  
Incremental batch processing  
Date-based S3 partitioning  
Parameterized AWS Glue job  
Conversion from CSV to Parquet  
No full data reloads  

Tech Stack  
AWS S3  
AWS Glue  
PySpark  
Parquet  

Status  
Incremental ingestion implemented  
Multiple partitions processed successfully  
Silver layer created with partitioned Parquet data  

Learning Outcome  
Built a production-style incremental ETL pipeline using AWS Glue and S3, similar to real-world enterprise data engineering workflows.
