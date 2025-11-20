# Dockerfile
# Use a lightweight Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /code

# Copy requirements first (for caching speed)
COPY ./requirements.txt /code/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the rest of the code
COPY ./app /code/app
COPY ./model_store /code/model_store

# Start the server
# host 0.0.0.0 exposes it to the outside world
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]