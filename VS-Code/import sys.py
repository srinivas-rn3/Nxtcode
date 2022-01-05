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

# Script generated for node Apply Mapping


# Script generated for node PostgreSQL
DataSink1 = glueContext.write_dynamic_frame.from_options(frame = AmazonS3_node1641389272287, connection_options = {"url": "jdbc:postgresql://database-glue-test.c43ukqrfsnyx.us-east-1.rds.amazonaws.com:5432/postgres", "user": "postgres", "password": "Password_12", "dbtable": "nextdb.marks"}, connection_type = 'postgresql')
job.commit()
