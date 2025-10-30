import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Optional: load credentials from .env if you set it up
load_dotenv()

# PostgreSQL connection details
DB_USER = os.getenv("PG_USER", "postgres")
DB_PASSWORD = os.getenv("PG_PASSWORD", "kesia")
DB_HOST = os.getenv("PG_HOST", "localhost")
DB_PORT = os.getenv("PG_PORT", "5432")
DB_NAME = os.getenv("PG_DB", "intern_db")

# Create SQLAlchemy engine
engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# Path to CSVs
DATA_PATH = "../data/raw"

# Tables and their files
tables = {
    "customers": "customers.csv",
    "products": "products.csv",
    "orders": "orders.csv",
    "order_items": "order_items.csv",
    "transactions": "transactions.csv"
}

# Loop through and load data
for table_name, filename in tables.items():
    file_path = os.path.join(DATA_PATH, filename)
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df.to_sql(table_name, engine, if_exists="replace", index=False)
        print(f"Loaded {len(df)} rows into table '{table_name}'")
    else:
        print(f"File not found: {file_path}")

print("All CSVs loaded into PostgreSQL successfully!")
