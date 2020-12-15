import pytest
from flask_jwt_extended import create_access_token

from .test_input import (
    complete_data,
    user,
)

"""
Tests for Create endpoint
"""


@pytest.mark.new
@pytest.mark.parametrize(
    "test_input",
    [
        (complete_data),
    ],
)
def test_create_success(client, _db, test_input):
    _db.session.add(user)
    _db.session.commit()
    access_token = create_access_token(user.id)
    headers = {"Authorization": access_token}
    response = client.post("/questionnaires/", headers=headers, json=test_input)
    json_response = response.get_json()

    assert response.status_code == 201
    assert json_response["user"] == str(user.id)
