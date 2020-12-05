from feather_simple_api import db
from sqlalchemy.ext.declarative import DeclarativeMeta

DbModel: DeclarativeMeta = db.Model
Db: DeclarativeMeta = db
