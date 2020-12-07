import pytest

from feather_simple_api import app, db


@pytest.fixture
def client(_db):
    _db.create_all()

    with app.test_client() as test_client:
        with app.app_context():
            yield test_client

    _db.drop_all()


@pytest.fixture
def _app():
    return app


@pytest.fixture
def _db():

    return db
