import os
from dotenv import load_dotenv

from feather_simple_api.core import create_app
from feather_simple_api.extensions.jwt_extended import (
    create_jwt_app,
    DEV_RSA_PRIVATE,
    DEV_RSA_PUBLIC,
)
from feather_simple_api.extensions.flask_sqlalchemy import (
    create_sqlalchemy_app,
    setup_guids_postgresql,
)

load_dotenv()

app = create_app(os.environ)

# jwt-extended related config
jwt = create_jwt_app(app)

app.config["JWT_PUBLIC_KEY"] = os.getenv("RSA_PUBLIC", DEV_RSA_PUBLIC)
app.config["JWT_PRIVATE_KEY"] = os.getenv("RSA_PRIVATE", DEV_RSA_PRIVATE)
app.config["JWT_ALGORITHM"] = "RS256"

# flask-sqlalchmey related config
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = create_sqlalchemy_app(app)
setup_guids_postgresql(db.engine)

# import models
from .models import User  # noqa: F401, E402

db.create_all()

# import route back
from .routes import app  # noqa: F401, E402
