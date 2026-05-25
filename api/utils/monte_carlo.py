import numpy as np


def run_monte_carlo(df, n_simulations=1000, seed=42):
    np.random.seed(seed)

    mean_loss = df['claim_amount'].mean()
    std_loss = df['claim_amount'].std()
    total_policies = len(df)

    results = []

    for _ in range(n_simulations):
        simulated_claims = np.random.normal(mean_loss, std_loss, total_policies)
        simulated_claims = np.clip(simulated_claims, 0, None)
        results.append(simulated_claims.sum())

    results = np.array(results)

    return {
        'mean': float(results.mean()),
        'std': float(results.std()),
        'p5': float(np.percentile(results, 5)),
        'p95': float(np.percentile(results, 95)),
        'p99': float(np.percentile(results, 99))
    }