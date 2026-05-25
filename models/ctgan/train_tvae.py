from sdv.single_table import TVAESynthesizer
from sdv.metadata import SingleTableMetadata
from sdv.evaluation.single_table import evaluate_quality

import pandas as pd
import pickle


# Load dataset
real_data = pd.read_csv('data/synthetic/baseline_auto.csv')


# Create metadata
metadata = SingleTableMetadata()
metadata.detect_from_dataframe(real_data)

metadata.update_column('fraud_flag', sdtype='categorical')
metadata.update_column('region', sdtype='categorical')
metadata.update_column('insurance_type', sdtype='categorical')


# Create TVAE model
model = TVAESynthesizer(
    metadata=metadata,
    epochs=300
)


# Train model
model.fit(real_data)


# Save trained model
with open('models/tvae/tvae_auto.pkl', 'wb') as f:
    pickle.dump(model, f)

print("TVAE model saved.")


# Generate synthetic data
synthetic_data = model.sample(num_rows=50000)

synthetic_data.to_csv(
    'data/synthetic/tvae_auto_50k.csv',
    index=False
)

print("Synthetic data generated and saved.")


# Evaluate quality
quality_report = evaluate_quality(
    real_data,
    synthetic_data,
    metadata
)

print("Quality Score:")
print(quality_report.get_score())