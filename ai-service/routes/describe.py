from flask import Blueprint, request, jsonify
from datetime import datetime
import time
import logging

from services.groq_client import call_groq
from services.fallback import fallback_describe
from middlewares.request_validator import validate_json_request
from config import DESCRIBE_PROMPT

# Configure logging
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

describe_bp = Blueprint('describe', __name__)


@describe_bp.route("/describe", methods=["POST"])
def describe():

    start_time = time.time()

    # Validate Content-Type
    validation = validate_json_request()

    if validation:
        return validation

    try:

        data = request.get_json()

        # Validate request body
        if not data:
            return jsonify({
                "success": False,
                "error": "Request body is required"
            }), 400

        # Get input text safely
        user_input = data.get("text")

        if not user_input:
            return jsonify({
                "success": False,
                "error": "Text field is required"
            }), 400

        user_input = user_input.strip()

        # Validate input length
        if len(user_input) < 5:
            return jsonify({
                "success": False,
                "error": "Input text is too short"
            }), 400

        if len(user_input) > 2000:
            return jsonify({
                "success": False,
                "error": "Input text exceeds limit"
            }), 400

        logger.info(f"Generating AI description for: {user_input}")

        # Build prompt messages
        messages = [
            {
                "role": "system",
                "content": DESCRIBE_PROMPT
            },
            {
                "role": "user",
                "content": user_input
            }
        ]

        # Call Groq API
        result = call_groq(messages, fallback_describe)

        # Generate embedding

        response_time = round(time.time() - start_time, 2)

        generated_at = datetime.utcnow().isoformat() + "Z"

        return jsonify({
            "success": True,
            "result": result["data"],
            "is_fallback": result["is_fallback"],
            "embedding_generated": embedding is not None,
            "generated_at": generated_at,
            "response_time": response_time
        }), 200

    except Exception as e:

        logger.error(f"/describe error: {str(e)}")

        return jsonify({
            "success": False,
            "error": "Failed to generate description"
        }), 500