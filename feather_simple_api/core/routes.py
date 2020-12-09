from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

# Import endpoints
from feather_simple_api.resources.auth import auth_endpoint
from feather_simple_api.resources.users import users_endpoint


def register_routes(app: Flask) -> None:
    limiter = Limiter(app, default_limits=["1/second"], key_func=get_remote_address)
    limiter.limit("80/minute")(users_endpoint.blueprint)

    app.register_blueprint(auth_endpoint.blueprint, url_prefix="/auth")  # type: ignore
    app.register_blueprint(users_endpoint.blueprint, url_prefix="/users")  # type: ignore
