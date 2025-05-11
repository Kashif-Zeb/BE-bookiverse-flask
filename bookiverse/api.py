from datetime import timedelta
import logging
from flask import Flask, jsonify
from flask_jwt_extended import JWTManager
from bookiverse.app.db import db
from bookiverse import config
import os
from http import HTTPStatus
from flask_migrate import Migrate
from celery import Celery
from bookiverse.blueprints.user import bp as user
from bookiverse.blueprints.flight import bp as flight
from bookiverse.blueprints.hotel import bp as hotel

from bookiverse.celery_settings import celery_init_app
from flask_mail import Mail
from .signals import user_logged_in
from .emails import send_login_email
from .email_initalize import mail
from .limiters import limiter,cache
from flask_limiter.errors import RateLimitExceeded
from flask_cors import CORS
migrate = Migrate()



def create_app():
    app = Flask(__name__)
    CORS(app,allow_origins=["*"])
    # app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///testing.db"
    # app.config[
    #     "SQLALCHEMY_DATABASE_URI"
    # ] = f"mysql+pymysql://{config.DB_USER}:{config.DB_PWD}@{config.DB_URL}:{config.DB_PORT}/{config.DB_NAME}"    #os.getenv("DATABASE_URI") for docker
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"mysql+pymysql://{config.DB_USER}:{config.DB_PWD}@{config.DB_URL}/{config.DB_NAME}"
    # app.config[
    #     "SQLALCHEMY_DATABASE_URI"
    # ] = "mysql+pymysql://root:kashif@localhost:3306/sms"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    app.config[
        "JWT_SECRET_KEY"
    ] = "60b8b427938bc9f2fbe65d98640e831b4a8522f56150b97f141677d02570819b"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(minutes=5) 
    UPLOAD_FOLDER = "uploads"
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    jwt = JWTManager(app)
    migrate.init_app(app, db)
    @app.errorhandler(HTTPStatus.BAD_REQUEST)
    @app.errorhandler(HTTPStatus.UNPROCESSABLE_ENTITY)
    # @app.errorhandler(HTTPStatus.TOO_MANY_REQUESTS)
    def webargs_error_handler(err):
        headers = err.data.get("headers", None)
        messages = err.data.get("messages", ["Invalid request."])
        if headers:
            return jsonify({"errors": messages}), err.code, headers
        else:
            return jsonify({"errors": messages}), err.code
    
    @app.errorhandler(RateLimitExceeded)
    def handle_too_many_requests(error):
        return jsonify(str(error)),error.code
    # with app.app_context():
    #     db.create_all()
    # celery = make_celery(app)
    app.config.from_mapping(
    CELERY=dict(
        broker_url="redis://localhost:6380",
        result_backend="redis://localhost:6380",
        task_ignore_result=True,
    ),
)
    celery_app = celery_init_app(app)

    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'kashifzeb19@gmail.com'
    # app.config['MAIL_PASSWORD'] = 
    app.config['MAIL_DEFAULT_SENDER'] = 'kashifzk216@gmail.com'

    mail.init_app(app)
    # limiter.init_app(app)

    app.config['CACHE_TYPE'] = 'SimpleCache'  # Use SimpleCache for demonstration
    app.config['CACHE_DEFAULT_TIMEOUT'] = 300
    cache.init_app(app)
    app.register_blueprint(user)
    app.register_blueprint(flight)
    app.register_blueprint(hotel)

    from bookiverse.app import models
    return app
