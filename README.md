# Predicting-Clinical-Significance-of-Human-Genetic-Variants
🧬 ClinVar Project — Phase 1: MongoDB Ingestion & Exploration
📌 Overview

This phase focuses on ingesting raw ClinVar genetic variant data into MongoDB and performing initial exploratory analysis using PyMongo aggregation pipelines.

The dataset is sourced from the ClinVar public archive, which contains human genetic variants and their clinical significance.

📂 Dataset
File: variant_summary.txt.gz
Source:
https://ftp.ncbi.nlm.nih.gov/pub/clinvar/tab_delimited/variant_summary.txt.gz
Format: TSV (Tab-Separated Values, gzipped)
Size: ~120MB compressed (~1GB uncompressed)
Records: ~2.5 million+
Key Columns Used
AlleleID
Type
GeneSymbol
ClinicalSignificance
Chromosome
Start
Stop
🎯 Objective (Phase 1)
Load raw TSV data into MongoDB using Python
Avoid using pandas (as per requirements)
Use batch insertion for performance
Perform basic exploratory queries using aggregation pipelines
⚙️ Tech Stack
Python 3
MongoDB (local server)
PyMongo
csv module (built-in)
gzip module (built-in)
🛠️ Setup Instructions
1. Install MongoDB

Download and install MongoDB Community Server:

👉 https://www.mongodb.com/try/download/community

2. Install Python Dependencies
pip install pymongo
3. Start MongoDB

Make sure MongoDB is running locally:

mongod
🚀 Data Ingestion

The dataset is read using Python’s csv.DictReader with gzip support and inserted into MongoDB in batches.

Key Approach:
Stream data line-by-line (memory efficient)
Convert each row into a dictionary
Insert documents in batches (5000–10000)
Example Snippet:
with gzip.open(FILE_PATH, mode="rt", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter="\t")

    batch = []
    for row in reader:
        batch.append(row)

        if len(batch) >= 5000:
            collection.insert_many(batch)
            batch = []

    if batch:
        collection.insert_many(batch)
📊 Exploratory Queries

The following queries were implemented using PyMongo aggregation pipelines as required:

1️⃣ Total Variant Count
collection.count_documents({})
2️⃣ Distribution of Variant Types
pipeline = [
    {
        "$group": {
            "_id": "$Type",
            "count": {"$sum": 1}
        }
    },
    {
        "$sort": {"count": -1}
    }
]
3️⃣ Variants per Chromosome
pipeline = [
    {
        "$group": {
            "_id": "$Chromosome",
            "count": {"$sum": 1}
        }
    },
    {
        "$sort": {"_id": 1}
    }
]
📈 Results

The queries provide:

Total number of genetic variants in the dataset
Distribution of variant types (e.g., SNV, deletion, insertion)
Number of variants per chromosome

These insights help understand the structure and distribution of the dataset before moving to large-scale processing.

🧠 Key Concepts Learned
Document-oriented data modeling in MongoDB
Efficient ingestion of large datasets using batch inserts
Streaming large files without loading into memory
Aggregation pipelines in MongoDB
Working with real-world biomedical datasets
⚠️ Notes
No use of pandas (project constraint)
Batch insertion is critical for performance
Data size is large → streaming approach is required
🔜 Next Phase

Phase 2 will involve:

Loading data into PySpark
Cleaning and transforming data
Performing advanced analytics using SparkSQL
