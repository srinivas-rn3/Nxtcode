import boto3
import pandas as pd

# Initialize AWS clients
s3_client = boto3.client('s3')
glue_client = boto3.client('glue')

# Define source and destination S3 bucket and keys
source_bucket = 'source-bucket-name'
source_key = 'source-folder/source-file.csv'
destination_bucket = 'destination-bucket-name'
destination_key = 'destination-folder/destination-file.csv'

# Extract data from source S3 bucket
response = s3_client.get_object(Bucket=source_bucket, Key=source_key)
source_data = pd.read_csv(response['Body'])

# Transform data (for demonstration purposes, let's just convert all text to uppercase)
transformed_data = source_data.applymap(lambda x: x.upper() if isinstance(x, str) else x)

# Load transformed data to destination S3 bucket
destination_data = transformed_data.to_csv(index=False)
s3_client.put_object(Body=destination_data, Bucket=destination_bucket, Key=destination_key)

# Start AWS Glue job to catalog the transformed data
glue_client.start_job_run(JobName='glue-job-name')
