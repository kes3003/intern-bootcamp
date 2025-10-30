import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta
import os

# Initialize Faker
fake = Faker()

# Ensure output folder exists
os.makedirs("data/raw", exist_ok=True)

# Number of records
NUM_CUSTOMERS = 50
NUM_PRODUCTS = 20
NUM_ORDERS = 100

# ---------- 1. CUSTOMERS ----------
customers = []
for i in range(1, NUM_CUSTOMERS + 1):
    customers.append({
        "customer_id": i,
        "name": fake.name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "city": fake.city(),
        "country": fake.country(),
        "created_at": fake.date_this_decade()
    })
customers_df = pd.DataFrame(customers)
customers_df.to_csv("data/raw/customers.csv", index=False)

# ---------- 2. PRODUCTS ----------
products = []
for i in range(1, NUM_PRODUCTS + 1):
    products.append({
        "product_id": i,
        "product_name": fake.word().title(),
        "category": random.choice(["Electronics", "Clothing", "Books", "Home", "Sports"]),
        "price": round(random.uniform(5, 500), 2),
        "stock": random.randint(10, 200)
    })
products_df = pd.DataFrame(products)
products_df.to_csv("data/raw/products.csv", index=False)

# ---------- 3. ORDERS ----------
orders = []
for i in range(1, NUM_ORDERS + 1):
    cust_id = random.randint(1, NUM_CUSTOMERS)
    order_date = datetime.now() - timedelta(days=random.randint(0, 365))
    orders.append({
        "order_id": i,
        "customer_id": cust_id,
        "order_date": order_date.date(),
        "status": random.choice(["Pending", "Shipped", "Delivered", "Cancelled"])
    })
orders_df = pd.DataFrame(orders)
orders_df.to_csv("data/raw/orders.csv", index=False)

# ---------- 4. ORDER ITEMS ----------
order_items = []
for order in orders:
    num_items = random.randint(1, 5)
    for _ in range(num_items):
        prod_id = random.randint(1, NUM_PRODUCTS)
        quantity = random.randint(1, 3)
        order_items.append({
            "order_id": order["order_id"],
            "product_id": prod_id,
            "quantity": quantity,
            "total_price": round(quantity * products_df.loc[products_df['product_id'] == prod_id, 'price'].values[0], 2)
        })
order_items_df = pd.DataFrame(order_items)
order_items_df.to_csv("data/raw/order_items.csv", index=False)

# ---------- 5. TRANSACTIONS ----------
transactions = []
for order in orders:
    transactions.append({
        "transaction_id": fake.uuid4(),
        "order_id": order["order_id"],
        "payment_method": random.choice(["Credit Card", "Debit Card", "PayPal", "UPI"]),
        "amount": round(random.uniform(20, 1000), 2),
        "transaction_date": order["order_date"]
    })
transactions_df = pd.DataFrame(transactions)
transactions_df.to_csv("data/raw/transactions.csv", index=False)

print("✅ Synthetic data generated successfully in data/raw/")
