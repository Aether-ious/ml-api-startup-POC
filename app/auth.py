# app/auth.py
from fastapi import Security, HTTPException, status
from fastapi.security.api_key import APIKeyHeader
import os

# Define the header key name (e.g., X-API-KEY: mysecretkey)
api_key_header = APIKeyHeader(name="X-API-KEY", auto_error=False)

def get_api_key(api_key_header: str = Security(api_key_header)):
    # In a real startup, you'd check a database of paid users here.
    # For MVP, we use an environment variable.
    REAL_API_KEY = os.getenv("API_SECRET", "default-dev-key") 
    
    if api_key_header == REAL_API_KEY:
        return api_key_header
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, 
            detail="Could not validate credentials"
        )