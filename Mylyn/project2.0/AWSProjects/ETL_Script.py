import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.sql import SparkSession

## @params: [TempDir, JOB_NAME]
args = getResolvedOptions(sys.argv, ['TempDir','JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

## Source Data
source_data = glueContext.create_dynamic_frame.from_catalog(database = "your_database_name", table_name = "your_table_name")

## Transformations
# Example transformation: Convert data types
transformed_data = ApplyMapping.apply(frame = source_data, mappings = [("column_name", "string", "new_column_name", "int")])

## Target Data
target_data = glueContext.write_dynamic_frame.from_options(frame = transformed_data, connection_type = "s3", connection_options = {"path": "s3://your_bucket/your_target_path"}, format = "parquet")

## Job Completed
job.commit()
