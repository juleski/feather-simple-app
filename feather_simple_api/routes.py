from . import app

# Import endpoints
from feather_simple_api.resources.auth import auth_endpoint

app.register_blueprint(auth_endpoint.blueprint, url_prefix="/auth")  # type: ignore
