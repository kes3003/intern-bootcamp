# Intern Bootcamp

This repository contains week-by-week data science practice modules.

## Structure
- `00_setup` – environment setup  
- `01_sdlc` – software development lifecycle  
- `02_sql` – relational data and queries  
- `03_mongo` – NoSQL and document data  
- `04_data_eng` – pipelines and automation  
- `05_analytics` – dashboards and insights  
- `06_ml` – machine learning fundamentals  
- `07_genai_rag` – retrieval-augmented generation  
- `08_chatbot` – conversational AI  
- `09_capstone` – final integrated project  
- `data/` – raw and processed datasets  
- `docs/` – reference and FAQs

---

## Week 1 – SDLC Foundations & Data Ingestion

### Implemented
- Created and activated a Python virtual environment (`venv/`).
- Installed core dependencies from `requirements.txt`.
- Configured `.env` for secure database credentials.
- Generated synthetic CSV data (`customers`, `products`, `orders`, `order_items`, `transactions`) under `data/raw/`.
- Loaded data into:
  - **PostgreSQL** (`intern_db` schema, 5 tables)
  - **MongoDB** (`intern_db` database, 5 collections)
- Implemented an ingestion script (`01_sdlc/ingest_csv.py`) that:
  - Reads CSVs using `pandas`
  - Performs validation (null checks, duplicates, schema mismatches)
  - Inserts records into PostgreSQL using `SQLAlchemy`
  - Logs every step to `logs/ingestion.log`
 
 