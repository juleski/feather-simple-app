import sys
from flask_sqlalchemy import SQLAlchemy

from .guid_type import setup_guids_postgresql


def create_sqlalchemy_app() -> SQLAlchemy:

    return SQLAlchemy()


def init_db(db: SQLAlchemy, drop_first: bool = False):
    try:
        if drop_first:
            db.drop_all()

        setup_guids_postgresql(db.engine)
        db.create_all()

    except Exception as e:
        print("An Error occured with initializing the DB")
        print("Make sure it is up and you are passing valid parameters\n")
        print(f"Exception is {str(e)}")
        sys.exit()
