import requests

BASE_URL = 'http://localhost:5000'


class TestAPIHealth:

    def test_kpis(self):

        response = requests.get(
            f'{BASE_URL}/api/kpis'
        )

        assert response.status_code == 200

        data = response.json()

        assert 'loss_ratio' in data
        assert 'fraud_rate' in data
        assert 'risk_score' in data


class TestFraudAPI:

    def test_fraud(self):

        response = requests.get(
            f'{BASE_URL}/api/fraud'
        )

        assert response.status_code == 200

        data = response.json()

        assert 'fraud_cases' in data
        assert 'fraud_rate' in data


class TestGeographicAPI:

    def test_geographic(self):

        response = requests.get(
            f'{BASE_URL}/api/geographic'
        )

        assert response.status_code == 200

        data = response.json()

        assert len(data) > 0


class TestSimulationAPI:

    def test_simulation(self):

        response = requests.get(
            f'{BASE_URL}/api/simulation/monte-carlo'
        )

        assert response.status_code == 200

        data = response.json()

        assert 'mean' in data
        assert 'p95' in data
        assert 'p99' in data


class TestDataPreviewAPI:

    def test_data_preview(self):

        response = requests.get(
            f'{BASE_URL}/api/data-preview'
        )

        assert response.status_code == 200

        data = response.json()

        assert 'rows' in data
        assert 'columns' in data
class TestComparisonAPI:

    def test_comparison(self):

        response = requests.get(
            f'{BASE_URL}/api/comparison'
        )

        assert response.status_code == 200

        data = response.json()

        assert 'results' in data
        assert 'summary' in data

        assert len(data['results']) > 0
        assert 'column' in data['results'][0]
        assert 'ctgan_wasserstein' in data['results'][0]
        assert 'tvae_wasserstein' in data['results'][0]

        assert 'best_model' in data['summary']
