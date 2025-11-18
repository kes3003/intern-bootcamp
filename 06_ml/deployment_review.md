# ML Deployment Review — Week 4  
### FastAPI • Streamlit • PostgreSQL • Batch Scoring • Drift Monitoring

- **API serving with FastAPI**
- **Interactive UI using Streamlit**
- **Batch scoring pipeline**
- **PostgreSQL storage**
- **Drift monitoring and reporting**

## 1. Real-Time API (FastAPI)

### Key Features
- Loads trained model: `best_model.pkl`
- `/health` endpoint for service status
- `/predict` endpoint for real-time inference
- Input validation using **Pydantic**
- Error handling with custom logging

### Example Request
'''json
{
  "Age": 30,
  "MonthlyIncome": 5000,
  "DistanceFromHome": 10,
  "JobSatisfaction": 3
}

### Example Response 
{"prediction": 0}

### Logging
All API errors & inputs recorded in:
api/api_logs.txt

## 2. User Interface (Streamlit) 

### Key Features
- Form with input fields
- Button triggers API call
- Prediction displayed in clean text

## 3. Batch Prediction Pipeline

### What it does

- Loads the HR dataset
- Loads the same model used by API
- Generates predictions + probabilities
- Inserts results into PostgreSQL table:
hr_batch_predictions

### Stored Columns

- employee_number
- prediction
- probability
- timestamp

Simulates nightly/weekly batch scoring in production.

## 4. Drift Monitoring

### What was compared

- Training dataset vs Batch inputs

### Findings

- No feature drift
- Strong prediction drift
- Training attrition ≈ 16%
- Batch predicted attrition = 0%
- Indicates model collapse (expected due to simplified 4-feature model)

### Output Report

Generated HTML saved at:
reports/drift_summary.html