import os

from flask import Flask
from flask_cors import CORS

from .routes import api_bp


def create_app() -> Flask:
    app = Flask(__name__)

    frontend_origin = os.getenv("FRONTEND_ORIGIN", "http://localhost:5173")
    CORS(app, resources={r"/api/*": {"origins": [frontend_origin]}})

    app.register_blueprint(api_bp, url_prefix="/api")
    return app
