from flask import jsonify, request
import logging

logger = logging.getLogger(__name__)


def register_error_handlers(app):

    @app.errorhandler(Exception)
    def handle_exception(e):

        logger.error(str(e))

        return jsonify({
            "error": "Internal server error"
        }), 500