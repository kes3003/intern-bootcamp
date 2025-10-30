import pandas as pd
from pymongo import MongoClient
import os

# Connection setup
client = MongoClient("mongodb://localhost:27017/")
db = client["intern_db"]

# Folder where your CSVs are stored
DATA_PATH = "../data/raw"

# List of CSV files to load
collections = {
    "customers": "customers.csv",
    "products": "products.csv",
    "orders": "orders.csv",
    "order_items": "order_items.csv",
    "transactions": "transactions.csv"
}

for collection_name, filename in collections.items():
    file_path = os.path.join(DATA_PATH, filename)
    
    if os.path.exists(file_path):
        # Read the CSV into a DataFrame
        df = pd.read_csv(file_path)
        
        # Convert DataFrame to dictionary format
        data_dict = df.to_dict(orient="records")
        
        # Insert into MongoDB
        collection = db[collection_name]
        collection.delete_many({})  # optional: clear old data
        collection.insert_many(data_dict)
        
        print(f"Inserted {len(data_dict)} records into '{collection_name}' collection.")
    else:
        print(f"File not found: {file_path}")

client.close()
print(" All CSVs loaded successfully into MongoDB!")
