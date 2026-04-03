# Predicting-Clinical-Significance-of-Human-Genetic-Variants
🧬 Lab – ClinVar Phase 1: MongoDB Ingestion and Exploration
📘 Overview

This project demonstrates handling large-scale datasets using MongoDB, Python, and aggregation pipelines.
It is divided into two main parts:

Data ingestion into MongoDB
Exploratory analysis using PyMongo

The dataset is sourced from ClinVar, a public archive of human genetic variants and their clinical significance.

#🧩 Part 1: Data Ingestion

This section focuses on loading a large TSV dataset into MongoDB efficiently.

Functions:

readDataset()

Reads the compressed dataset (.gz) using gzip and parses it using csv.DictReader.

batchInsert()

Inserts records into MongoDB in batches (5000–10000 documents) to improve performance.

cleanRow()

Processes each row before insertion (e.g., handling empty values).

🧩 Part 2: Exploratory Analysis

This section focuses on analyzing the stored data using MongoDB aggregation pipelines.

Functions:

getTotalCount()

Returns the total number of variants stored in the database.

getVariantTypeDistribution()

Groups variants by Type and counts occurrences of each variant type.

getVariantsPerChromosome()

Groups variants by Chromosome and sorts the results.

⚙️ Technologies Used
Python
MongoDB
PyMongo
