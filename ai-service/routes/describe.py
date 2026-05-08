from flask import Blueprint, request, jsonify

from services.groq_client import call_groq
from services.chroma_service import search_documents

describe_bp = Blueprint('describe', __name__)

@describe_bp.route('/describe', methods=['POST'])
def describe():

    data = request.get_json()

    title = data.get("title", "")
    description = data.get("description", "")

    # Combine input
    user_input = f"{title} {description}"

    # Search knowledge base
    knowledge = search_documents(user_input)

    # Extract context
    context = ""

    if knowledge and knowledge.get("documents"):
        context = " ".join(knowledge["documents"][0])

    # Build AI prompt
    prompt = f"""
    You are a sustainability compliance AI assistant.

    Use the following sustainability knowledge while generating the response:

    {context}

    Issue Title:
    {title}

    Issue Description:
    {description}

    Generate a professional sustainability compliance description.
    """

    # Call Groq AI
    ai_response = call_groq(prompt)

    return jsonify({
        "response": ai_response["data"]["raw_text"]
    })