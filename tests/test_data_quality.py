import pandas as pd
import numpy as np
from scipy import stats


def test_synthetic_data_schema():
    df = pd.read_csv('data/synthetic/ctgan_auto_50k.csv')

    required_columns = [
        'policy_id',
        'premium',
        'claim_amount',
        'fraud_flag',
        'region'
    ]

    for col in required_columns:
        assert col in df.columns, f'Missing column: {col}'

    assert len(df) >= 10000, 'Dataset too small'
    assert df['fraud_flag'].isin([0, 1]).all(), 'fraud_flag must be 0 or 1'
    assert (df['premium'] > 0).all(), 'All premiums must be positive'
    assert (df['claim_amount'] >= 0).all(), 'Claims cannot be negative'


def test_no_missing_values():
    df = pd.read_csv('data/synthetic/ctgan_auto_50k.csv')

    assert df.isnull().sum().sum() == 0, 'Dataset contains missing values'


def test_numeric_columns_valid():
    df = pd.read_csv('data/synthetic/ctgan_auto_50k.csv')

    numeric_columns = ['premium', 'claim_amount']

    for col in numeric_columns:
        assert np.isfinite(df[col]).all(), f'{col} contains invalid numeric values'


def test_region_values_valid():
    df = pd.read_csv('data/synthetic/ctgan_auto_50k.csv')

    valid_regions = ['Punjab', 'Sindh', 'KPK', 'Balochistan', 'AJK', 'GB']

    assert df['region'].isin(valid_regions).all(), 'Invalid region found'