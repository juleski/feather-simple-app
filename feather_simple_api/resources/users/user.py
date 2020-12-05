from datetime import datetime

from feather_simple_api import DbModel, Db

from feather_simple_api.extensions.flask_sqlalchemy import (
    GUID,
    GUID_SERVER_DEFAULT_POSTGRESQL,
)


class User(DbModel):
    __tablename__ = "users"

    id = Db.Column(
        GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL
    )
    email = Db.Column(Db.String(120), unique=True, nullable=False)
    password = Db.Column(Db.String(255), nullable=False)
    created = Db.Column(Db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.email}"
