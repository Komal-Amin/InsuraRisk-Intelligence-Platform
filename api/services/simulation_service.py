from api.utils.data_loader import load_dataset
from api.utils.monte_carlo import run_monte_carlo


def generate_monte_carlo_results():

    df = load_dataset()

    results = run_monte_carlo(df)

    return results