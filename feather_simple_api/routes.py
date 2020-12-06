from . import app

# Import endpoints
from feather_simple_api.resources.auth import auth_endpoint
from feather_simple_api.resources.users import users_endpoint

# test
app.register_blueprint(auth_endpoint.blueprint, url_prefix="/auth")  # type: ignore
app.register_blueprint(users_endpoint.blueprint, url_prefix="/users")  # type: ignore
