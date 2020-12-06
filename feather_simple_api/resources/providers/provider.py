from datetime import datetime

from feather_simple_api import DbModel, Db

from feather_simple_api.extensions.flask_sqlalchemy import (
    GUID,
    GUID_SERVER_DEFAULT_POSTGRESQL,
)
from feather_simple_api.resources.users.enums import OccupationStatus


class Provider(DbModel):
    __tablename__ = "providers"

    id = Db.Column(
        GUID, primary_key=True, server_default=GUID_SERVER_DEFAULT_POSTGRESQL
    )
    name = Db.Column(Db.String(120), nullable=True)
    price = Db.Column(Db.Float())
    billing_period = Db.Column(Db.String(255), default="per month")
    for_occupation = Db.Column(Db.Enum(OccupationStatus), nullable=True)
    created = Db.Column(Db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Provider {self.name}"
