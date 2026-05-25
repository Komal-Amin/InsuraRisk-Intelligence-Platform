import numpy as np
from flask import Flask, jsonify, request 
from flask_cors import CORS 
import pandas as pd 
import os 
from dotenv import load_dotenv
from api.routes.metrics import metrics_bp
from api.routes.simulation import simulation_bp
from api.routes.fraud import fraud_bp
from api.routes.geographic import geo_bp
from api.routes.data_explorer import data_bp
from api.routes.comparison import comparison_bp
 
# Load environment variables from .env file 
load_dotenv() 
 
# Create the Flask app 
app = Flask(__name__) 
app.register_blueprint(metrics_bp)
app.register_blueprint(simulation_bp)
app.register_blueprint(fraud_bp)
app.register_blueprint(geo_bp)
app.register_blueprint(data_bp)
app.register_blueprint(comparison_bp)
CORS(app)  # Allow dashboard to call the API (Cross-Origin Resource Sharing)
# Load synthetic datasets into memory when the app starts 
DATA_PATH = os.getenv('SYNTHETIC_DATA_PATH', './data/synthetic/') 
datasets = {} 
 
def load_datasets(): 
    for fname in ['ctgan_auto_50k.csv', 'ctgan_health_50k.csv', 
'ctgan_property_50k.csv']: 
        name = fname.replace('.csv', '') 
        fpath = DATA_PATH + fname 
        if os.path.exists(fpath): 
            datasets[name] = pd.read_csv(fpath) 
load_datasets() 
 
# ENDPOINT 1: Health check — is the API running? 
@app.route('/api/health', methods=['GET']) 
def health(): 
    return jsonify({'status': 'ok', 'datasets_loaded': list(datasets.keys())}) 
 
# ENDPOINT 2: Get all KPI metrics 
@app.route('/api/metrics', methods=['GET']) 
def get_metrics(): 
    dataset_name = request.args.get('dataset', 'ctgan_auto_50k') 
    if dataset_name not in datasets: 
        return jsonify({'error': 'Dataset not found'}), 404 
    df = datasets[dataset_name] 
    # Loss ratio = total claims / total premium (key insurance KPI) 
    loss_ratio = df['claim_amount'].sum() / df['premium'].sum() 
    fraud_rate = df['fraud_flag'].mean() 
    return jsonify({ 
        'loss_ratio': round(loss_ratio, 4), 
        'fraud_rate': round(fraud_rate, 4), 
        'total_policies': len(df),})

@app.route('/api/monte-carlo')
def monte_carlo():
    dataset = request.args.get('dataset', 'ctgan_auto_50k')
    df = datasets[dataset]

    mean_loss = df['claim_amount'].mean()
    std_loss = df['claim_amount'].std()
    total_policies = len(df)

    results = []

    for i in range(1000):
        simulated_claims = np.random.normal(mean_loss, std_loss, total_policies)
        simulated_claims = np.clip(simulated_claims, 0, None)
        results.append(simulated_claims.sum())

    results = np.array(results)

    return jsonify({
        'mean': float(results.mean()),
        'std': float(results.std()),
        'p5': float(np.percentile(results, 5)),
        'p95': float(np.percentile(results, 95)),
        'p99': float(np.percentile(results, 99))
    })

if __name__ == '__main__': 
    app.run(debug=True, port=5000)