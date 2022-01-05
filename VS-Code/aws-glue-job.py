import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Amazon S3
AmazonS3_node1641389272287 = glueContext.create_dynamic_frame.from_options(
    format_options={"quoteChar": '"', "withHeader": True, "separator": ","},
    connection_type="s3",
    format="csv",
    connection_options={
        "paths": [
            "s3://db-mirgration-2112/migration-0501/NEXTDB/MARKS/LOAD00000001.csv"
        ],
        "recurse": True,
    },
    transformation_ctx="AmazonS3_node1641389272287",
)
AmazonS3_df1 = glueContext.create_dynamic_frame.from_options(
    format_options={"quoteChar": '"', "withHeader": True, "separator": ","},
    connection_type="s3",
    format="csv",
    connection_options={
        "paths": [
            "s3://db-mirgration-2112/migration-0501/NEXTDB/STUDENTS/LOAD00000001.csv"
        ],
        "recurse": True,
    },
    transformation_ctx="AmazonS3_node1641389272287",
)

AmazonS3_df2 = glueContext.create_dynamic_frame.from_options(
    format_options={"quoteChar": '"', "withHeader": True, "separator": ","},
    connection_type="s3",
    format="csv",
    connection_options={
        "paths": [
            "s3://db-mirgration-2112/migration-0501/NEXTDB/MODULES/LOAD00000001.csv"
        ],
        "recurse": True,
    },
    transformation_ctx="AmazonS3_node1641389272287",
)
# Script generated for node Apply Mapping


# Script generated for node PostgreSQL
PostgreSQL_node1641389308109 = glueContext.write_dynamic_frame.from_catalog(
    frame=AmazonS3_node1641389272287,
    database="pg-db-dest",
    table_name="nextdb_public_marks",
    transformation_ctx="PostgreSQL_node1641389308109",
)
PostgreSQL_df3 = glueContext.write_dynamic_frame.from_catalog(
    frame=AmazonS3_df1,
    database="pg-db-dest",
    table_name="nextdb_public_student",
    transformation_ctx="PostgreSQL_node1641389308109",
)
PostgreSQL_df3 = glueContext.write_dynamic_frame.from_catalog(
    frame=AmazonS3_df2,
    database="pg-db-dest",
    table_name="nextdb_public_modules",
    transformation_ctx="PostgreSQL_node1641389308109",
)
job.commit()
