!pip install pymongo
import csv
import gzip
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
print("Connected successfully")

db = client["clinvar_db"]
collection = db["variants"]

collection.drop()
print("!Old collection dropped!")

batch = []
batch_size = 5000

with gzip.open(r"C:\Users\HP\Desktop\big data project\variant_summary.txt.gz", "rt") as file:
    reader = csv.DictReader(file)

    for row in reader:
        batch.append(row)

        if len(batch) >= batch_size:
            collection.insert_many(batch)
            print(f"Inserted {len(batch)} records")
            batch = []

    if batch:
        collection.insert_many(batch)
        print(f"Inserted final {len(batch)} records")

print("Data loading completed")
