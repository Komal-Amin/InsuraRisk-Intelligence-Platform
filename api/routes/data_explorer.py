from flask import Blueprint, jsonify
from api.services.data_service import generate_data_preview

data_bp = Blueprint('data_bp', __name__)


@data_bp.route('/api/data-preview')
def data_preview():

    results = generate_data_preview()

    return jsonify(results)