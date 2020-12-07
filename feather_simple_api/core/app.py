import os
import secrets

from typing import Union, Dict
from flask import Flask


def create_app(user_config: Union[os._Environ, Dict]) -> Flask:
    app = Flask(__name__)

    for app_conf in app.config:
        if app_conf == "SECRET_KEY":
            app.config[app_conf] = user_config.get(app_conf, secrets.token_urlsafe(16))
        else:
            app.config[app_conf] = user_config.get(app_conf, app.config[app_conf])

    return app
