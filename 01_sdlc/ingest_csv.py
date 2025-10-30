import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import logging

# -----------------------------------------------------------------------------
# 1. Setup logging
# -----------------------------------------------------------------------------
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/ingestion.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Starting CSV ingestion process...")

# -----------------------------------------------------------------------------
# 2. Load environment variables
# -----------------------------------------------------------------------------
load_dotenv()
DB_USER = os.getenv("PG_USER")
DB_PASSWORD = os.getenv("PG_PASSWORD")
DB_HOST = os.getenv("PG_HOST")
DB_PORT = os.getenv("PG_PORT")
DB_NAME = os.getenv("PG_DB")

# -----------------------------------------------------------------------------
# 3. Create SQLAlchemy connection
# -----------------------------------------------------------------------------
try:
    engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    conn = engine.connect()
    logging.info("Database connection established successfully.")
except Exception as e:
    logging.error(f"Database connection failed: {e}")
    raise

# -----------------------------------------------------------------------------
# 4. Define data folder & target tables
# -----------------------------------------------------------------------------
DATA_PATH = "../data/raw"
TABLES = {
    "customers": "customers.csv",
    "products": "products.csv",
    "orders": "orders.csv",
    "order_items": "order_items.csv",
    "transactions": "transactions.csv"
}

# -----------------------------------------------------------------------------
# 5. Helper: validate dataframe
# -----------------------------------------------------------------------------
def validate_dataframe(df: pd.DataFrame, table_name: str):
    issues = []

    # Null check
    nulls = df.isnull().sum()
    if nulls.any():
        issues.append(f"Null values found in {table_name}: {nulls[nulls>0].to_dict()}")

    # Duplicates
    if df.duplicated().any():
        issues.append(f"Duplicate rows found in {table_name}: {df[df.duplicated()].shape[0]} rows")

    # Schema check: just ensures it’s not empty
    if df.empty:
        issues.append(f"{table_name} is empty or not readable")

    return issues

# -----------------------------------------------------------------------------
# 6. Main loop: read → validate → load
# -----------------------------------------------------------------------------
for table, filename in TABLES.items():
    path = os.path.join(DATA_PATH, filename)

    if not os.path.exists(path):
        logging.warning(f"File not found: {path}")
        continue

    try:
        df = pd.read_csv(path)
        logging.info(f"Loaded {filename} ({len(df)} rows)")

        # Validation
        problems = validate_dataframe(df, table)
        if problems:
            for issue in problems:
                logging.warning(issue)
        else:
            logging.info(f"Validation passed for {table}")

        # Load to PostgreSQL
        df.to_sql(table, engine, if_exists="replace", index=False)
        logging.info(f"💾 Inserted {len(df)} rows into {table}")

    except Exception as e:
        logging.error(f"Error processing {filename}: {e}")

# -----------------------------------------------------------------------------
# 7. Cleanup
# -----------------------------------------------------------------------------
conn.close()
engine.dispose()
logging.info("Ingestion completed successfully.")
print("Data ingestion complete! Check logs/ingestion.log for details.")
