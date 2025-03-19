import joblib
import numpy as np
import pandas as pd

def load_model_and_predict(model_type, input_data):
    model = joblib.load(f'./models/{model_type}_model.joblib')
    scaler = joblib.load(f'./models/{model_type}_scaler.joblib')

    df = pd.DataFrame([input_data])
    features = ['CRSDepHour', 'CRSArrHour', 'Airline', 'Origin', 'Dest', 'DepDelay', 'TaxiOut']
    X_scaled = scaler.transform(df[features])
    prediction = model.predict(X_scaled)
    return prediction[0]