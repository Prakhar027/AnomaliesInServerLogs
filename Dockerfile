# 1. Use an official Python base image
FROM python:3.11-slim

# 2. Set the working directory
WORKDIR /app

# 3. Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of the app
COPY . .

# 5. Expose the port FastAPI runs on
EXPOSE 8000

# 6. Run the FastAPI app with uvicorn
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
