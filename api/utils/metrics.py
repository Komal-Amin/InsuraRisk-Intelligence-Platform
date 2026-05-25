def calculate_loss_ratio(total_claims, total_premium):
    return total_claims / total_premium


def calculate_combined_ratio(total_claims, expenses, total_premium):
    return (total_claims + expenses) / total_premium


def calculate_fraud_rate(fraud_cases, total_claims):
    return fraud_cases / total_claims


def calculate_risk_score(loss_ratio, fraud_rate):
    score = (loss_ratio * 70) + (fraud_rate * 30)
    return round(score * 100, 2)