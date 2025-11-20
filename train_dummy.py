# train_dummy.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import joblib
import os

# 1. Create dummy data (Simulating Credit Risk: Income, Debt, Credit Score)
X, y = make_classification(n_samples=1000, n_features=3, n_informative=3, 
                           n_redundant=0, random_state=42)

# 2. Train Model
clf = RandomForestClassifier()
clf.fit(X, y)

# 3. Save Model
os.makedirs("model_store", exist_ok=True)
joblib.dump(clf, "model_store/model_v1.pkl")

print("✅ Model trained and saved to model_store/model_v1.pkl")