import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)
## @type: DataSource
## @args: [database = "s3-data", table_name = "students", transformation_ctx = "datasource0"]
## @return: datasource0
## @inputs: []
#datasource0 = glueContext.create_dynamic_frame.from_catalog(database = "s3-data", table_name = "students", transformation_ctx = "datasource0")
#datasource1 = glueContext.create_dynamic_frame.from_catalog(database = "s3-data", table_name = "marks", transformation_ctx = "datasource1")
#datasource2 = glueContext.create_dynamic_frame.from_catalog(database = "s3-data", table_name = "modules", transformation_ctx = "datasource2")

#df = glueContext.create_dynamic_frame.from_options(connection_options = {"paths": "s3://db-mirgration-2112/migration-0501/NEXTDB/MARKS/", "recurse":True}, transformation_ctx = "df")
df = glueContext.create_dynamic_frame.from_options(connection_type = "s3", format = "csv" ,connection_options = {"paths": "s3://db-mirgration-2112/migration-0501/NEXTDB/MARKS/LOAD00000001.csv", "recurse":True}, transformation_ctx = "df")

## @type: ApplyMapping
## @args: [mapping = [("student_no", "long", "student_no", "long"), ("surname", "string", "surname", "string"), ("forename", "string", "forename", "string")], transformation_ctx = "applymapping1"]
## @return: applymapping1
## @inputs: [frame = datasource0]
#applymapping1 = ApplyMapping.apply(frame = datasource0, mappings = [("student_no", "long", "student_no", "long"), ("surname", "string", "surname", "string"), ("forename", "string", "forename", "string")], transformation_ctx = "applymapping1")
## @type: ResolveChoice
## @args: [choice = "make_cols", transformation_ctx = "resolvechoice2"]
## @return: resolvechoice2
## @inputs: [frame = applymapping1]
#resolvechoice2 = ResolveChoice.apply(frame = applymapping1, choice = "make_cols", transformation_ctx = "resolvechoice2")
## @type: DropNullFields
## @args: [transformation_ctx = "dropnullfields3"]
## @return: dropnullfields3
## @inputs: [frame = resolvechoice2]
#dropnullfields3 = DropNullFields.apply(frame = resolvechoice2, transformation_ctx = "dropnullfields3")
## @type: DataSink
## @args: [catalog_connection = "pg-dest-1", connection_options = {"dbtable": "students", "database": "nextdb"}, transformation_ctx = "datasink4"]
## @return: datasink4
## @inputs: [frame = dropnullfields3]
#datasink4 = glueContext.write_dynamic_frame.from_jdbc_conf(frame = datasource0, catalog_connection = "pg-dest-1", connection_options = {"dbtable": "students", "database": "nextdb"}, transformation_ctx = "datasink4")
datasink5 = glueContext.write_dynamic_frame.from_jdbc_conf(frame = df, catalog_connection = "pg-dest-1", connection_options = {"dbtable": "marks", "database": "nextdb"}, transformation_ctx = "datasink5")
#datasink6 = glueContext.write_dynamic_frame.from_jdbc_conf(frame = datasource0, catalog_connection = "pg-dest-1", connection_options = {"dbtable": "modules", "database": "nextdb"}, transformation_ctx = "datasink6")
job.commit()