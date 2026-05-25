import pandas as pd
from scipy.stats import ks_2samp, wasserstein_distance


def compare_real_synthetic():
    real = pd.read_csv('data/synthetic/baseline_auto.csv')
    ctgan = pd.read_csv('data/synthetic/ctgan_auto_50k.csv')
    tvae = pd.read_csv('data/synthetic/tvae_auto_50k.csv')

    columns = ['premium', 'claim_amount']
    results = []

    for col in columns:
        ctgan_ks = ks_2samp(real[col], ctgan[col])
        tvae_ks = ks_2samp(real[col], tvae[col])

        results.append({
            'column': col,
            'ctgan_ks_pvalue': float(ctgan_ks.pvalue),
            'tvae_ks_pvalue': float(tvae_ks.pvalue),
            'ctgan_wasserstein': float(wasserstein_distance(real[col], ctgan[col])),
            'tvae_wasserstein': float(wasserstein_distance(real[col], tvae[col])),
            'real_mean': float(real[col].mean()),
            'ctgan_mean': float(ctgan[col].mean()),
            'tvae_mean': float(tvae[col].mean())
        })

    ctgan_avg_distance = sum(r['ctgan_wasserstein'] for r in results) / len(results)
    tvae_avg_distance = sum(r['tvae_wasserstein'] for r in results) / len(results)

    best_model = 'CTGAN' if ctgan_avg_distance < tvae_avg_distance else 'TVAE'

    return {
        'results': results,
        'summary': {
            'ctgan_avg_wasserstein': float(ctgan_avg_distance),
            'tvae_avg_wasserstein': float(tvae_avg_distance),
            'best_model': best_model
        }
    }