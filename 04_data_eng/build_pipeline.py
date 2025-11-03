import os
import pandas as pd
import logging
from datetime import datetime

# --- Logging Setup ---
os.makedirs("04_data_eng/logs", exist_ok=True)
log_file = "04_data_eng/logs/pipeline.log"

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    encoding="utf-8", 
    format="%(asctime)s | %(levelname)s | %(message)s",
)

# --- Utility Functions ---
def validate_dataframe(df: pd.DataFrame, name: str):
    """Perform basic validations: nulls, duplicates, and dtypes."""
    logging.info(f"Validating {name}...")
    report = {}

    # Count nulls
    report["null_values"] = df.isnull().sum().sum()

    # Count duplicates
    report["duplicates"] = df.duplicated().sum()

    # Check dtypes
    report["dtypes"] = df.dtypes.to_dict()

    logging.info(f"{name} — Nulls: {report['null_values']}, Duplicates: {report['duplicates']}")
    return df.drop_duplicates(), report


def transform_and_save(file_path: str, output_folder: str):
    """Read CSV, validate, and save as Parquet."""
    name = os.path.basename(file_path).replace(".csv", "")
    try:
        df = pd.read_csv(file_path)
        df, validation_report = validate_dataframe(df, name)

        # Example transformations
        df.columns = [col.strip().lower() for col in df.columns]
        df = df.convert_dtypes()

        # Output paths
        os.makedirs(output_folder, exist_ok=True)
        output_file = os.path.join(output_folder, f"{name}_clean.parquet")

        df.to_parquet(output_file, index=False)

        logging.info(f"{name}: Processed {len(df)} rows → {output_file}")
        logging.info(f"Validation Summary: {validation_report}")

    except Exception as e:
        logging.error(f"Error processing {name}: {e}")


# --- Main Pipeline ---
def main():
    logging.info("Starting Data Engineering Pipeline")

    raw_folder = "data/raw"
    processed_folder = "data/processed"

    for file in os.listdir(raw_folder):
        if file.endswith(".csv"):
            transform_and_save(os.path.join(raw_folder, file), processed_folder)

    logging.info("Pipeline completed successfully.")


if __name__ == "__main__":
    main()
