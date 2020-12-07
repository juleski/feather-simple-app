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
from sqlalchemy.ext.declarative import DeclarativeMeta

load_dotenv()

app = create_app(os.environ)

# jwt-extended related config
jwt = create_jwt_app(app)

app.config["JWT_PUBLIC_KEY"] = os.getenv("RSA_PUBLIC", DEV_RSA_PUBLIC)
app.config["JWT_PRIVATE_KEY"] = os.getenv("RSA_PRIVATE", DEV_RSA_PRIVATE)
app.config["JWT_ALGORITHM"] = "RS256"
app.config["JWT_HEADER_TYPE"] = os.getenv("JWT_HEADER_TYPE", "")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = os.getenv("JWT_ACCESS_TOKEN_EXPIRES", 3600)

# flask-sqlalchmey related config
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = create_sqlalchemy_app(app)
setup_guids_postgresql(db.engine)

DbModel: DeclarativeMeta = db.Model
Db: DeclarativeMeta = db

# import models
from .models import *  # noqa: F401, F403, E402

db.create_all()

# import route back
from .routes import app  # noqa: F401, E402
