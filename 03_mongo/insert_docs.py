from pymongo import MongoClient
from pprint import pprint

client = MongoClient("mongodb://localhost:27017")
db = client["intern_db"]

new_customers = [
    {"customer_id": 601, "name": "Arun Mehta", "country": "India"},
    {"customer_id": 602, "name": "Sara Lee", "country": "UAE"}
]
result = db.customers.insert_many(new_customers)
print(f"Inserted {len(result.inserted_ids)} customers:\n")

for customer in new_customers:
    pprint(customer)