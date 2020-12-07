import pytest

from .test_input import (
    complete_data,
    data_without_email,
    data_without_firstname,
    data_without_address,
    data_without_occupation,
    data_without_has_child,
)


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
def test_required_fields_error(client, test_input, expected):
    response = client.post("/users/", json=test_input)
    json_response = response.get_json()

    assert response.status_code == 422
    assert "error" in json_response
    assert json_response["error"] == expected
