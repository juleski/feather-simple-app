from datetime import datetime

from feather_simple_api import DbModel, Db

from feather_simple_api.extensions.flask_sqlalchemy import (
    GUID,
    GUID_SERVER_DEFAULT_POSTGRESQL,
)
from .enums import OccupationStatus


class User(DbModel):
    __tablename__ = "users"

    id = Db.Column(
        GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL
    )
    password = Db.Column(Db.String(255), nullable=True)
    email = Db.Column(Db.String(120), nullable=False)
    firstname = Db.Column(Db.String(120), nullable=True)
    address = Db.Column(Db.String(255), nullable=True)
    occupation = Db.Column(Db.Enum(OccupationStatus), nullable=True)
    has_child = Db.Column(Db.Boolean, nullable=True)
    child_num = Db.Column(Db.Integer, nullable=True)
    created = Db.Column(Db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.email}"
