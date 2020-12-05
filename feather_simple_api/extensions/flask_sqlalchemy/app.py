from flask_sqlalchemy import SQLAlchemy
from flask import Flask


def create_sqlalchemy_app(app: Flask) -> SQLAlchemy:

    return SQLAlchemy(app)
