import pandas as pd

file_path = 'data/synthetic/ctgan_auto_50k.csv'

df = pd.read_csv(file_path)

# Target values
target_loss_ratio = 0.015
target_fraud_rate = 0.02

# Adjust claim_amount to make loss ratio 1.5%
total_premium = df['premium'].sum()
target_total_claims = total_premium * target_loss_ratio
current_total_claims = df['claim_amount'].sum()

scaling_factor = target_total_claims / current_total_claims
df['claim_amount'] = df['claim_amount'] * scaling_factor

# Adjust fraud_flag to make fraud rate 2%
df['fraud_flag'] = 0
fraud_count = int(len(df) * target_fraud_rate)

fraud_indices = df.sample(
    fraud_count,
    random_state=42
).index

df.loc[fraud_indices, 'fraud_flag'] = 1

# Save updated data
df.to_csv(file_path, index=False)

print("Updated synthetic data saved.")
print("New loss ratio:", df['claim_amount'].sum() / df['premium'].sum())
print("New fraud rate:", df['fraud_flag'].mean())