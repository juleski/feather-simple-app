import os
from dotenv import load_dotenv

from feather_simple_api.core import create_app
from feather_simple_api.extensions.jwt_extended import create_jwt_app
from feather_simple_api.extensions.flask_sqlalchemy import create_sqlalchemy_app
from sqlalchemy.ext.declarative import DeclarativeMeta


load_dotenv()

db = create_sqlalchemy_app()
jwt = create_jwt_app()
app = create_app(os.environ, db=db, jwt=jwt)

DbModel: DeclarativeMeta = db.Model
Db: DeclarativeMeta = db

# import route back
from feather_simple_api.core.routes import register_routes  # noqa: F401, E402

register_routes(app)
