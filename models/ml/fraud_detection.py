from sklearn.ensemble import IsolationForest
import pandas as pd
import numpy as np


def detect_fraud(df, contamination=0.05):
    # Select only numeric features for the model
    features = df[['premium', 'claim_amount']].values

    # contamination=0.05 means we expect 5% fraud
    model = IsolationForest(
        n_estimators=100,
        contamination=contamination,
        random_state=42
    )

    model.fit(features)

    # Predict: -1 = anomaly, 1 = normal
    df['anomaly_score'] = model.decision_function(features)
    df['predicted_fraud'] = (model.predict(features) == -1).astype(int)

    return df


if __name__ == "__main__":
    df = pd.read_csv('data/synthetic/ctgan_auto_50k.csv')

    result = detect_fraud(df)

    result.to_csv('data/processed/fraud_detected_auto.csv', index=False)

    print("Fraud detection completed.")
    print("Saved to data/processed/fraud_detected_auto.csv")
    print(result[['policy_id', 'premium', 'claim_amount', 'predicted_fraud']].head())
