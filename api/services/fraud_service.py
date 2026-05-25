import pandas as pd


def generate_fraud_results():

    df = pd.read_csv(
    'data/processed/fraud_detected_auto.csv'
)

    fraud_cases = df[
        df['predicted_fraud'] == 1
    ]

    return {
        'total_records': int(len(df)),
        'fraud_cases': int(len(fraud_cases)),
        'fraud_rate': float(
            len(fraud_cases) / len(df)
        ),
        'top_fraud_records': fraud_cases[
            [
                'policy_id',
                'premium',
                'claim_amount',
                'anomaly_score'
            ]
        ].head(10).to_dict(orient='records')
    }
