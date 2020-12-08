import os
import secrets

from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from typing import Union, Dict
from flask import Flask

from feather_simple_api.extensions.jwt_extended import (
    DEV_RSA_PRIVATE,
    DEV_RSA_PUBLIC,
)
from .error_handler import register_error_handlers


def create_app(
    user_config: Union[os._Environ, Dict], db: SQLAlchemy = None, jwt: JWTManager = None
) -> Flask:

    app = Flask(__name__)

    # Register error handlers
    register_error_handlers(app)

    for app_conf in app.config:
        if app_conf == "SECRET_KEY":
            app.config[app_conf] = user_config.get(app_conf, secrets.token_urlsafe(16))
        else:
            app.config[app_conf] = user_config.get(app_conf, app.config[app_conf])

    app.app_context().push()
    if db:
        # flask-sqlalchmey related config
        app.config["SQLALCHEMY_DATABASE_URI"] = user_config.get(
            "SQLALCHEMY_DATABASE_URI", None
        )
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        db.init_app(app)

    if jwt:
        # jwt-extended related config
        app.config["JWT_PUBLIC_KEY"] = user_config.get("RSA_PUBLIC", DEV_RSA_PUBLIC)
        app.config["JWT_PRIVATE_KEY"] = user_config.get("RSA_PRIVATE", DEV_RSA_PRIVATE)
        app.config["JWT_ALGORITHM"] = "RS256"
        app.config["JWT_HEADER_TYPE"] = user_config.get("JWT_HEADER_TYPE", "")
        app.config["JWT_ACCESS_TOKEN_EXPIRES"] = user_config.get(
            "JWT_ACCESS_TOKEN_EXPIRES", 3600
        )
        jwt.init_app(app)

    return app
