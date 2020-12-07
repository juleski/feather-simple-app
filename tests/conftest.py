import pytest

from feather_simple_api import app


@pytest.fixture
def client():

    with app.test_client() as test_client:
        with app.app_context():
            yield test_client
