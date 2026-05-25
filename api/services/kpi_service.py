from api.utils.data_loader import load_dataset
from api.utils.logger import log_info


def generate_kpis():

    df = load_dataset()
    log_info('Generating KPI metrics')

    total_claims = df['claim_amount'].sum()
    total_premium = df['premium'].sum()

    loss_ratio = total_claims / total_premium

    fraud_cases = df['fraud_flag'].sum()

    fraud_rate = fraud_cases / len(df)

    combined_ratio = (
        total_claims + 1000000
    ) / total_premium

    risk_score = (
        (loss_ratio * 70) +
        (fraud_rate * 30)
    ) * 100

    return {
        'loss_ratio': round(loss_ratio, 4),
        'combined_ratio': round(combined_ratio, 4),
        'fraud_rate': round(fraud_rate, 4),
        'risk_score': round(risk_score, 2)
    }