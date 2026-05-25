from flask import Blueprint, jsonify
from api.services.kpi_service import generate_kpis

metrics_bp = Blueprint('metrics_bp', __name__)


@metrics_bp.route('/api/kpis')
def get_kpis():

    kpis = generate_kpis()

    return jsonify(kpis)
