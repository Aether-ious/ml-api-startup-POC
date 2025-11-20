# app/schemas.py
from pydantic import BaseModel

# What you expect the client to send
class CreditScoringInput(BaseModel):
    feature_1: float  # e.g., Income
    feature_2: float  # e.g., Debt
    feature_3: float  # e.g., Credit Score

# What you promise to send back
class PredictionOutput(BaseModel):
    risk_class: int
    probability: float
    message: str