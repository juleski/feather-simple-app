import pytest
from flask_jwt_extended import create_access_token
from feather_simple_api.constants import PROVIDER_EXCLUDE_KEYS
from feather_simple_api.resources.providers.provider_dto import ProviderDto

from .test_input import (
    complete_data,
    data_without_email,
    data_without_firstname,
    data_without_address,
    data_without_occupation,
    data_without_has_child,
    user,
    provider1,
    provider2,
)

"""
Tests for Create endpoint
"""


@pytest.mark.integration
@pytest.mark.parametrize(
    "test_input",
    [
        (complete_data),
    ],
)
def test_create_success(client, test_input):
    response = client.post("/users/", json=test_input)
    json_response = response.get_json()

    assert response.status_code == 201
    assert json_response["user"]["email"] == test_input["email"]


@pytest.mark.integration
@pytest.mark.parametrize(
    "test_input,expected",
    [
        (data_without_email, ["email field required"]),
        (data_without_firstname, ["firstname field required"]),
        (data_without_address, ["address field required"]),
        (data_without_occupation, ["occupation field required"]),
        (data_without_has_child, ["has_child field required"]),
    ],
)
def test_required_fields_error_on_create(client, test_input, expected):
    response = client.post("/users/", json=test_input)
    json_response = response.get_json()

    assert response.status_code == 422
    assert "error" in json_response
    assert json_response["error"] == expected


"""
Tests for Recommendation endpoint
"""


@pytest.mark.integration
def test_can_get_recommendations(client, _db):
    _db.session.add(user)
    _db.session.add(provider1)
    _db.session.add(provider2)
    _db.session.commit()

    exepected = [ProviderDto.from_orm(provider1), ProviderDto.from_orm(provider2)]
    exepected = [item.dict(exclude=PROVIDER_EXCLUDE_KEYS) for item in exepected]
    access_token = create_access_token(user.id)
    headers = {"Authorization": access_token}
    response = client.get("/users/recommendations", headers=headers)

    json_response = response.get_json()

    assert response.status_code == 200
    assert "recommendations" in json_response
    assert json_response["recommendations"] == exepected


@pytest.mark.integration
def test_recommendations_without_auth_header(client):

    response = client.get("/users/recommendations")

    assert response.status_code == 401
