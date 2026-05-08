# Sustainability Compliance Monitor — AI Service

## Overview

This AI microservice powers the Sustainability Compliance Monitor capstone project.

The service uses:
- Flask
- Groq LLaMA models
- ChromaDB
- Redis caching
- Docker

It generates:
- sustainability issue descriptions
- ESG recommendations
- compliance reports

---

# Tech Stack

- Python 3.11
- Flask 3.x
- Groq API
- ChromaDB
- Sentence Transformers
- Redis
- Docker

---

# Folder Structure

ai-service/
│
├── routes/
├── services/
├── knowledge/
├── test_inputs/
├── middlewares/
├── prompts/
├── app.py
├── Dockerfile
├── requirements.txt
└── README.md

---

# Environment Variables

Create `.env`

Example:

GROQ_API_KEY=your_groq_api_key
REDIS_HOST=redis
REDIS_PORT=6379
FLASK_ENV=development
PORT=5000

---

# Docker Setup

## Build Container

docker build -t sustainability-ai-service .

## Run Container

docker run -p 5000:5000 sustainability-ai-service

---

# Docker Compose

From project root:

docker-compose up --build

---

# Health Endpoint

GET /health

Example:

http://localhost:5000/health

Response:

{
  "status": "healthy",
  "service": "ai-service"
}

---

# API Endpoints

## 1. POST /describe

Generate sustainability issue descriptions.

### Request

{
  "title": "Waste Overflow",
  "description": "Waste exceeded monthly threshold"
}

### Response

{
  "response": "AI-generated sustainability analysis"
}

---

## 2. POST /recommend

Generate sustainability recommendations.

### Request

{
  "issue": "High electricity usage"
}

### Response

{
  "response": "AI-generated sustainability recommendations"
}

---

## 3. POST /generate-report

Generate sustainability compliance reports.

### Request

{
  "records": [
    {
      "title": "Water Usage",
      "status": "HIGH"
    }
  ]
}

### Response

{
  "response": "AI-generated sustainability report"
}

---

# Knowledge Base

The AI service uses:
- ChromaDB
- sustainability domain documents
- semantic search

Knowledge files are stored in:

knowledge/

---

# Security Features

- Input validation
- Prompt injection filtering
- Rate limiting
- Security headers
- ZAP-tested endpoints

---

# Running Tests

Run:

python test_prompts.py

---

# Performance

Average API response times:

| Endpoint | Avg Time |
|---|---|
| /describe | 1.3s |
| /recommend | 1.4s |
| /generate-report | 1.8s |

---

# Author

AI Developer 1 — Sustainability Compliance Monitor Capstone Project