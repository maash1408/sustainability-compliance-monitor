from flask import request, jsonify


def validate_json_request():

    if not request.is_json:
        return jsonify({
            "error": "Content-Type must be application/json"
        }), 400

    return None

