from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
print("Connected successfully")

db = client["test_db"]
collection = db["test_collection"]

collection.insert_one({"name": "Ahmad", "status": "working"})
print("Inserted successfully")
