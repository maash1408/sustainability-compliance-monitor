from flask import Blueprint, request, jsonify

from services.groq_client import call_groq
from config import REPORT_PROMPT

report_bp = Blueprint('report', __name__)

@report_bp.route('/generate-report', methods=['POST'])
def generate_report():

    data = request.get_json()

    records = data.get("records", [])

    if not records:
        return jsonify({
            "error": "Invalid input"
        }), 400

    formatted_records = ""

    for record in records:
        formatted_records += (
            f"Title: {record.get('title', '')}\n"
            f"Status: {record.get('status', '')}\n\n"
        )

    prompt = f"""
    {REPORT_PROMPT}

    Sustainability Records:

    {formatted_records}

    Generate a professional sustainability compliance report.
    """

    ai_response = call_groq(prompt)

    return jsonify({
        "response": ai_response["data"]["raw_text"]
    })