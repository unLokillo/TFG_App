from enum import unique
from msilib import sequence
from turtle import position
from flask import Flask, request, jsonify, json, session
from flask_api import status
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_login import LoginManager
from flask_session import Session
import os

db = SQLAlchemy()
ma = Marshmallow()
login_manager = LoginManager()
s = Session()


def create_app():
    # Construct the core app object.
    app = Flask(__name__, instance_relative_config=False)

    # CORS
    Cors = CORS(app)
    CORS(app, resources={r'/*': {'origins': '*'}},
         CORS_SUPPORTS_CREDENTIALS=True)

    # Application Configuration
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    ma.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        from . import routes
        from . import auth

        # Register Blueprints
        app.register_blueprint(routes.main_bp)
        app.register_blueprint(auth.auth_bp)

        # Create Database Models
        db.create_all()

        s.init_app(app)

        return app
