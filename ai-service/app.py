from flask import Flask, jsonify, request
from routes.describe import describe_bp
from routes.recommend import recommend_bp
from routes.generate_report import report_bp
from middlewares.security_headers import apply_security_headers

from routes.security_headers import register_security_headers
app = Flask(__name__)
register_security_headers(app)




# Register routes
app.register_blueprint(describe_bp)
app.register_blueprint(recommend_bp)
app.register_blueprint(report_bp)

apply_security_headers(app)

app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024

@app.route('/')
def home():
    return jsonify({
        "message": "Sustainability AI Service Running"
    }), 200

@app.route('/health', methods=['GET'])
def health():
    return jsonify({
        "status": "healthy",
        "service": "ai-service"
    }), 200

@app.after_request
def remove_server_header(response):
    response.headers['Server'] = 'SecureServer'
    return response

@app.before_request
def validate_request_size():
    max_size = 1024 * 1024

    if request.content_length and request.content_length > max_size:
        return jsonify({"error": "Request too large"}), 413

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)