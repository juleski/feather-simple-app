import os
from dotenv import load_dotenv

from feather_simple_api.core import create_app
from feather_simple_api.extensions.jwt_extended import (
    create_jwt_app,
    DEV_RSA_PRIVATE,
    DEV_RSA_PUBLIC,
)

load_dotenv()

app = create_app(os.environ)

# jwt-extended related config
jwt = create_jwt_app(app)

app.config["JWT_PUBLIC_KEY"] = os.getenv("RSA_PUBLIC", DEV_RSA_PUBLIC)
app.config["JWT_PRIVATE_KEY"] = os.getenv("RSA_PRIVATE", DEV_RSA_PRIVATE)
app.config["JWT_ALGORITHM"] = "RS256"

# import route back
from .routes import app  # noqa: F401, E402
