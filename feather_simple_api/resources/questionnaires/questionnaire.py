from datetime import datetime

from feather_simple_api import DbModel, Db

from feather_simple_api.extensions.flask_sqlalchemy import (
    GUID,
    GUID_SERVER_DEFAULT_POSTGRESQL,
)


class Questionnaire(DbModel):
    __tablename__ = "questionnaires"

    id = Db.Column(
        GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL
    )
    user = Db.Column(GUID, Db.ForeignKey("users.id"), nullable=False)
    email = Db.Column(Db.String(120), nullable=False)
    firstname = Db.Column(Db.String(120))
    address = Db.Column(Db.String(255))
    occupation = Db.Column(Db.String(255))
    has_child = Db.Column(Db.Boolean)
    child_num = Db.Column(Db.Integer, default=0)
    created = Db.Column(Db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<User {self.email}"
