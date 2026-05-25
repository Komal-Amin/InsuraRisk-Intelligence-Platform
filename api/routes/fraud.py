from flask import Blueprint, jsonify
from api.services.fraud_service import generate_fraud_results

fraud_bp = Blueprint('fraud_bp', __name__)


@fraud_bp.route('/api/fraud')
def fraud_results():

    results = generate_fraud_results()

    return jsonify(results)