import numpy as np
import pandas as pd


def run_monte_carlo(df, n_simulations=1000, seed=42):

    np.random.seed(seed)

    results = []

    # Get historical loss statistics from synthetic data
    mean_loss = df['claim_amount'].mean()
    std_loss = df['claim_amount'].std()
    total_policies = len(df)

    for sim in range(n_simulations):

        # Simulate claim amounts
        simulated_claims = np.random.normal(
            mean_loss,
            std_loss,
            total_policies
        )

        # No negative claims
        simulated_claims = np.clip(simulated_claims, 0, None)

        total_loss = simulated_claims.sum()

        results.append(total_loss)

    results = np.array(results)

    return {
        'mean': float(results.mean()),
        'std': float(results.std()),
        'p5': float(np.percentile(results, 5)),
        'p95': float(np.percentile(results, 95)),
        'p99': float(np.percentile(results, 99)),
        'simulations': results.tolist()
    }


if __name__ == "__main__":

    df = pd.read_csv('data/synthetic/ctgan_auto_50k.csv')

    results = run_monte_carlo(df)

    print("\n=== Monte Carlo Results ===")
    print(f"Mean Loss: {results['mean']:,.2f}")
    print(f"Standard Deviation: {results['std']:,.2f}")
    print(f"5th Percentile (Best Case): {results['p5']:,.2f}")
    print(f"95th Percentile (Worst Case): {results['p95']:,.2f}")
    print(f"99th Percentile (Catastrophe): {results['p99']:,.2f}")