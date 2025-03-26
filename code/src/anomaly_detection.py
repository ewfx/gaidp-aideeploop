from sklearn.ensemble import IsolationForest
import pandas as pd

def detect_anomalies(df):
    # Assuming 'amount' is the column to check for anomalies
    model = IsolationForest(contamination=0.05)
    df['anomaly'] = model.fit_predict(df[['amount']])
    anomalies = df[df['anomaly'] == -1]
    return anomalies
