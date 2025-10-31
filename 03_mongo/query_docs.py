from pymongo import MongoClient
from pprint import pprint

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["intern_db"]

# STEP 1 — Rename "product_name" → "name" if needed
rename_result = db.products.update_many(
    {"product_name": {"$exists": True}},
    [
        {"$set": {"name": "$product_name"}},
        {"$unset": "product_name"}
    ]
)
if rename_result.modified_count > 0:
    print(f"Renamed {rename_result.modified_count} documents from 'product_name' → 'name'\n")

# STEP 2 — Query customers
print(" Indian customers:\n")
for doc in db.customers.find({"country": "India"}, {"_id": 0, "name": 1, "country": 1}):
    pprint(doc)

# STEP 3 — Query products
print("\n Products (sorted by price):\n")
for doc in db.products.find({}, {"_id": 0, "name": 1, "price": 1, "category": 1}).sort("price", -1):
    pprint(doc)
