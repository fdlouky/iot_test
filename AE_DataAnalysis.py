from pymongo import MongoClient
from pyspark.sql import SparkSession
from pyspark.sql import functions as f

client = MongoClient('localhost', port=27017)

# List MongoDB databases
print(client.list_database_names())
# Use or create a MongoDB database
db = client['db_elastacloud']
# Create a new MongoDB collection
col = db['collection_elastacloud']

# List collection names
print(db.list_collection_names())

# Count the number of documents in the collection
col.count_documents({})

# Show all the documents in my database
# for doc in col.find({}):
#     print(doc,"\n")

# Connect spark to MongoDB
my_spark = SparkSession \
    .builder \
    .appName("myApp") \
    .config('spark.jars.packages','org.mongodb.spark:mongo-spark-connector_2.11:2.2.0' ) \
    .config("spark.mongodb.input.uri", "mongodb://127.0.0.1/db_elastacloud.collection_elastacloud") \
    .config("spark.mongodb.output.uri", "mongodb://127.0.0.1/db_elastacloud.collection_elastacloud") \
    .getOrCreate()

# Load all the data from MongoDB to Spark Dataframe
df = my_spark.read.format("com.mongodb.spark.sql.DefaultSource").load()
df.printSchema()
df.show()

# Load documents from device_name 1000002 from MongoDB to Spark Dataframe
pipeline = "{'$match': {'device_name': 1000002}}"
df2 = my_spark.read.format("com.mongodb.spark.sql.DefaultSource").option("pipeline", pipeline).load()
df2.show()

# Calculate some statistics for each device from their latitude and longitude
analysis = df.groupBy(df.device_name).agg(
f.min("device_latitude").alias("min_Latitude"),f.min("device_longitude").alias("min_Longitude"),
f.mean("device_latitude").alias("mean_Latitude"),f.mean("device_longitude").alias("mean_Longitude"),
f.max("device_latitude").alias("max_Latitude"),f.max("device_longitude").alias("max_Longitude"))
analysis.show()

