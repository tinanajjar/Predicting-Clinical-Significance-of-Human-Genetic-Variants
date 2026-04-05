!pip install pymongo
import csv
import gzip
from pymongo import MongoClient


#Part 1 — Ingestion
#Reads the dataset file
#Converts each row into a MongoDB document
#Inserts data in batches (5000 rows at a time)

client = MongoClient("mongodb://localhost:27017/")
print("Connected successfully")

db = client["clinvar_db"]
collection = db["variants"]

collection.drop()
print("!Old collection dropped!")

batch = []
batch_size = 5000

with gzip.open(r"C:\Users\HP\Desktop\big data project\variant_summary.txt.gz", "rt") as file:
    reader = csv.DictReader(file, delimiter="\t")

    for row in reader:
        batch.append(row)

        if len(batch) >= batch_size:
            collection.insert_many(batch)
            #print(f"Inserted {len(batch)} records")
            batch = []

    if batch:
        collection.insert_many(batch)
        print(f"Inserted final {len(batch)} records")

print("Data loading completed")

# Aggregation pipeline:
# Group data by "Type" and count how many records per type
pipeline = [
    {"$group" : {
        "_id" : "$Type", # group by Type column
        "count" : {"$sum" : 1} # count number of rows in each group
    }
    },
    {"$sort" : {"count" : -1} # sort results from highest to lowest count
    }
]

# Run the aggregation query
results = collection.aggregate(pipeline)

# Print the results
for doc in results:
    print(doc)
