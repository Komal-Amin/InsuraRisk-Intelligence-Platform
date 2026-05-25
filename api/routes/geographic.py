from flask import Blueprint, jsonify
from api.services.geographic_service import generate_geographic_summary

geo_bp = Blueprint('geo_bp', __name__)


@geo_bp.route('/api/geographic')
def geographic_data():

    results = generate_geographic_summary()

    return jsonify(results)