from flask import Blueprint, request, jsonify
from services.groq_client import call_groq
from config import RECOMMEND_PROMPT

recommend_bp = Blueprint('recommend', __name__)

@recommend_bp.route('/recommend', methods=['POST'])
def recommend():

    data = request.get_json()

    issue = data.get("issue", "")

    if not issue:
        return jsonify({
            "error": "Invalid input"
        }), 400

    prompt = f"""
    {RECOMMEND_PROMPT}

    Sustainability Issue:
    {issue}

    Generate professional sustainability recommendations.
    """

    ai_response = call_groq(prompt)

    return jsonify({
        "response": ai_response["data"]["raw_text"]
    })