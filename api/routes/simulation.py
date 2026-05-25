from flask import Blueprint, jsonify
from api.services.simulation_service import generate_monte_carlo_results

simulation_bp = Blueprint('simulation_bp', __name__)


@simulation_bp.route('/api/simulation/monte-carlo')
def monte_carlo_route():

    results = generate_monte_carlo_results()

    return jsonify(results)