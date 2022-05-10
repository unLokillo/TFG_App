"""Flask app configuration."""
from datetime import timedelta
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Set Flask configuration from environment variables."""

    FLASK_APP = 'wsgi.py'
    FLASK_ENV = environ.get('FLASK_ENV')
    SECRET_KEY = 'fmVb@st^jCP7f$uM' # environ.get('SECRET_KEY')

    # Flask-Assets
    LESS_BIN = environ.get('LESS_BIN')
    ASSETS_DEBUG = environ.get('ASSETS_DEBUG')
    LESS_RUN_IN_DEBUG = environ.get('LESS_RUN_IN_DEBUG')

    # Static Assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    COMPRESSOR_DEBUG = environ.get('COMPRESSOR_DEBUG')

    # Flask-SQLAlchemy
    basedir = path.abspath(path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + path.join(basedir, 'db.sqlite')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # CORS
    CORS_HEADERS = 'Content-Type'

    #Files
    DEFAULT_FOLDER = path.join(basedir, 'assets/')

    #Session
    SESSION_TYPE = 'filesystem'
    SESSION_COOKIE_PATH = '/'
    APPLICATION_ROOT = '/'
    SESSION_COOKIE_SAMESITE = "None"
    SESSION_COOKIE_SECURE = True
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=20)

    # Email
    MAIL_SERVER='smtp.sendgrid.net'
    MAIL_PORT = 587
    MAIL_USERNAME = 'apikey'
    MAIL_PASSWORD = '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'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False