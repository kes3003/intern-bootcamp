import pandas as pd
import joblib
import psycopg2
from datetime import datetime
import logging

# ------------------------------------------------------
# Logging setup
# ------------------------------------------------------
logging.basicConfig(
    filename="batch_logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

logging.info("HR Batch prediction started")

# ------------------------------------------------------
# 1. Load HR Employee Attrition Dataset
# ------------------------------------------------------
df = pd.read_csv("../HR-Employee-Attrition.csv")

# ------------------------------------------------------
# 2. Load the trained ML model
# ------------------------------------------------------
model = joblib.load("../api/best_model.pkl")

# ------------------------------------------------------
# 3. Select the exact 4 features used in training
# ------------------------------------------------------
features = ["Age", "MonthlyIncome", "DistanceFromHome", "JobSatisfaction"]
batch_X = df[features]

# ------------------------------------------------------
# 4. Run predictions
# ------------------------------------------------------
df["prediction"] = model.predict(batch_X)
df["probability"] = model.predict_proba(batch_X)[:, 1]
df["batch_timestamp"] = datetime.now()

logging.info(f"Predictions completed for {len(df)} employees")

# ------------------------------------------------------
# 5. Save results to PostgreSQL
# ------------------------------------------------------
try:
    conn = psycopg2.connect(
        dbname="intern_db",
        user="postgres",
        password="kesia",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()

    # Create table if not exists
    cur.execute("""
        CREATE TABLE IF NOT EXISTS hr_batch_predictions (
            employee_number INT,
            prediction INT,
            probability FLOAT,
            batch_timestamp TIMESTAMP
        );
    """)

    # Insert rows
    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO hr_batch_predictions (employee_number, prediction, probability, batch_timestamp)
            VALUES (%s, %s, %s, %s)
        """, (
            int(row["EmployeeNumber"]),
            int(row["prediction"]),
            float(row["probability"]),
            row["batch_timestamp"]
        ))

    conn.commit()
    logging.info("Batch results saved to PostgreSQL successfully.")

except Exception as e:
    logging.error(f"Database error: {str(e)}")

finally:
    if "conn" in locals():
        conn.close()


