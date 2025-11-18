from fastapi import FastAPI
from pydantic import BaseModel, Field
import joblib
import pandas as pd


from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import logging
import traceback


# -----------------------------
# 1. Create FastAPI app
# -----------------------------
app = FastAPI(title="ML Model API")

# Enable logging
logging.basicConfig(filename="api_logs.txt", level=logging.ERROR, format="%(asctime)s - %(message)s")

# CORS 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global error handler
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    error_message = f"Error: {str(exc)} | Path: {request.url.path}"
    logging.error(error_message)
    logging.error(traceback.format_exc())

    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error. Check logs."},
    )

# -----------------------------
# 2. Load your trained model
# -----------------------------
model = joblib.load("best_model.pkl")

# -----------------------------
# 3. Input Schema (Validation)
# -----------------------------
class InputData(BaseModel):
    Age: int = Field(..., ge=18, le=70, description="Employee age must be between 18 and 70")
    MonthlyIncome: float = Field(..., ge=0, description="Income must be non-negative")
    DistanceFromHome: float = Field(..., ge=0, description="Distance must be non-negative")
    JobSatisfaction: float = Field(..., ge=1, le=4, description="JobSatisfaction must be between 1 and 4")

# -----------------------------
# 4. Health Check Endpoint
# -----------------------------
@app.get("/health")
def health_check():
    return {"status": "API is running!"}


# -----------------------------
# 5. Prediction Endpoint
# -----------------------------
class PredictionOutput(BaseModel):
    prediction: int

@app.post("/predict", response_model=PredictionOutput)
def predict(data: InputData):
    try:
        df = pd.DataFrame([{
            "Age": data.Age,
            "MonthlyIncome": data.MonthlyIncome,
            "DistanceFromHome": data.DistanceFromHome,
            "JobSatisfaction": data.JobSatisfaction
        }])

        prediction = model.predict(df)[0]
        return {"prediction": int(prediction)}

    except Exception as e:
        logging.error(f"Prediction error: {str(e)}")
        raise e

