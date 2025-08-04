import pandas as pd
from sklearn.ensemble import IsolationForest
import pickle

df = pd.read_csv("data/server_logs.csv")

df['ip_encoded'] = df['ip'].astype('category').cat.codes
features = df[['ip_encoded', 'response_time', 'status_code']]

model = IsolationForest(contamination=0.02, random_state=42)
model.fit(features)

with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)
