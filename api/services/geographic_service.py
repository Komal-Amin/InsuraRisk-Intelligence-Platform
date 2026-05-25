from api.utils.data_loader import load_dataset


def generate_geographic_summary():

    df = load_dataset()

    summary = df.groupby('region').agg({
        'claim_amount': 'mean',
        'fraud_flag': 'mean',
        'policy_id': 'count'
    }).reset_index()

    summary.columns = [
        'region',
        'average_claim_amount',
        'fraud_rate',
        'total_policies'
    ]

    return summary.to_dict(orient='records')