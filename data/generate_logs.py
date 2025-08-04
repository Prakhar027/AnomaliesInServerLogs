import random
import pandas as pd
from datetime import datetime, timedelta

def generate_logs(num_logs=500):
    logs = []
    ip_pool = ['192.168.1.' + str(i) for i in range(1, 10)]

    for _ in range(num_logs):
        log = {
            'ip': random.choice(ip_pool),
            'timestamp': datetime.now() - timedelta(minutes=random.randint(0, 500)),
            'response_time': abs(random.gauss(100, 20)),
            'status_code': random.choices([200, 200, 200, 500, 404], [80, 10, 5, 3, 2])[0],
        }
        logs.append(log)

    for _ in range(10):
        log = {
            'ip': '10.0.0.' + str(random.randint(1, 5)),
            'timestamp': datetime.now(),
            'response_time': random.randint(500, 1000),
            'status_code': 500,
        }
        logs.append(log)

    df = pd.DataFrame(logs)
    df.to_csv("data/server_logs.csv", index=False)

if __name__ == "__main__":
    generate_logs()
