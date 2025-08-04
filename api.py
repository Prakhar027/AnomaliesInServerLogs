from fastapi import FastAPI
import pandas as pd
import pickle

app = FastAPI()
model = pickle.load(open("model/model.pkl", "rb"))

@app.get("/")
def root():
    return {"message": "Log Anomaly Detection API"}

@app.post("/predict/")
def predict(ip: str, response_time: float, status_code: int):
    ip_code = hash(ip) % 10
    features = pd.DataFrame([[ip_code, response_time, status_code]],
                            columns=['ip_encoded', 'response_time', 'status_code'])
    prediction = model.predict(features)[0]
    result = "anomaly" if prediction == -1 else "normal"
    return {"result": result}
