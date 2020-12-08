import pytest

from feather_simple_api import db
from feather_simple_api.core import create_app
from feather_simple_api.extensions.jwt_extended import create_jwt_app
from feather_simple_api.core.routes import register_routes  # noqa: F401, E402
from feather_simple_api.extensions.flask_sqlalchemy import init_db

from .config import test_config


@pytest.fixture
def app(request):
    jwt = create_jwt_app()
    app = create_app(test_config, db=db, jwt=jwt)
    register_routes(app)
    with app.app_context():
        init_db(db)

        yield app

    @request.addfinalizer
    def drop_tables():
        db.drop_all()


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def _db():

    return db
