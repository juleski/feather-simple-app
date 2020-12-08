import pytest

from werkzeug.exceptions import UnprocessableEntity

from feather_simple_api.resources.users.users_service import UsersService
from feather_simple_api.resources.users.validators import UserBody
from .test_input import user_dto, complete_data, provider_dto


@pytest.mark.unit
def test_create(mocker):
    class MockUsersDao:
        def create(self, params):
            return user_dto

    service = UsersService(UsersDao=MockUsersDao)
    params = UserBody(**complete_data)
    test_token = "test_token"

    mocker.patch(
        "feather_simple_api.resources.users.users_service.create_access_token",
        return_value=test_token,
    )
    response = service.create(params=params)

    assert response.access_token == test_token
    assert response.user == user_dto


@pytest.mark.unit
def test_get_recommendations(mocker):
    class MockUsersDao:
        def get_by_id(self, id):
            return user_dto

    class MockProvidersDao:
        def get_providers(self, filter_exp):
            return [provider_dto]

    service = UsersService(UsersDao=MockUsersDao, ProvidersDao=MockProvidersDao)

    response = service.get_recommendations(user_id=user_dto.id)

    assert response == [provider_dto]


def test_get_recommendations_invalid_user(mocker):
    class MockUsersDao:
        def get_by_id(self, id):
            return None

    class MockProvidersDao:
        def get_providers(self, filter_exp):
            return []

    service = UsersService(UsersDao=MockUsersDao, ProvidersDao=MockProvidersDao)
    expected = None
    try:
        service.get_recommendations(user_id=user_dto.id)
    except Exception as e:
        expected = e

    assert isinstance(expected, UnprocessableEntity)
    assert expected.description == "User does not exist"
