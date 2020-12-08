from flask_sqlalchemy import SQLAlchemy


def create_sqlalchemy_app() -> SQLAlchemy:

    return SQLAlchemy()
