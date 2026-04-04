# ingestion.py
import csv
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["clinvarDB"]
collection = db["variants"]

with open("Dataset/file.tsv", "r") as file:
    reader = csv.DictReader(file, delimiter="\t")
    
    batch = []
    for i, row in enumerate(reader):
        batch.append(row)
        
        if len(batch) == 5000:
            collection.insert_many(batch)
            batch = []

    if batch:
        collection.insert_many(batch)

print("Data inserted successfully!")
