from flask import Blueprint, request, jsonify
from database import insert_log

http_blueprint = Blueprint('http', __name__)

@http_blueprint.route('/log', methods=['POST'])
def log():
    """Endpoint HTTP pour recevoir un log."""
    log_data = request.get_json()
    if not log_data or not all(k in log_data for k in ['time_agent', 'host', 'ip', 'input']):
        return jsonify({"error": "Invalid log data"}), 400

    if insert_log(log_data, method="HTTP"):
        return jsonify({"status": "success"}), 201
    else:
        return jsonify({"error": "Failed to insert log"}), 500
