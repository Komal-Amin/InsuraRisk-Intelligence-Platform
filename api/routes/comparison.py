from flask import Blueprint, jsonify
from api.services.comparison_service import compare_real_synthetic

comparison_bp = Blueprint('comparison_bp', __name__)


@comparison_bp.route('/api/comparison')
def comparison_results():
    results = compare_real_synthetic()
    return jsonify(results)