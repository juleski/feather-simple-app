import os
import secrets

from flask import Flask


def create_app(config: os._Environ) -> Flask:
    app = Flask(__name__)

    app.config["secret"] = config.get("SECRET", secrets.token_urlsafe(16))

    return app
