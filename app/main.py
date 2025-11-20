# app/main.py
from fastapi import FastAPI, Depends, HTTPException
from contextlib import asynccontextmanager
import joblib
import pandas as pd
from app.schemas import CreditScoringInput, PredictionOutput
from app.auth import get_api_key

# Global variable to hold the model
ml_models = {}

# Lifespan event: Load model on startup, not on every request
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load model
    try:
        ml_models["risk_model"] = joblib.load("model_store/model_v1.pkl")
        print("✅ Model loaded successfully.")
    except Exception as e:
        print(f"❌ Failed to load model: {e}")
    yield
    # Clean up resources (if needed)
    ml_models.clear()

app = FastAPI(title="My AI Startup API", lifespan=lifespan)

@app.get("/")
def health_check():
    return {"status": "running", "service": "Model-as-a-Service v1"}

@app.post("/predict", response_model=PredictionOutput)
def predict(payload: CreditScoringInput, api_key: str = Depends(get_api_key)):
    
    # 1. Check if model exists
    if "risk_model" not in ml_models:
        raise HTTPException(status_code=500, detail="Model not loaded")
    
    # 2. Prepare data (convert Pydantic schema to DataFrame)
    data = [[payload.feature_1, payload.feature_2, payload.feature_3]]
    
    # 3. Inference
    model = ml_models["risk_model"]
    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0].max()
    
    # 4. Return Result
    return {
        "risk_class": int(prediction),
        "probability": float(probability),
        "message": "High Risk" if prediction == 1 else "Low Risk"
    }