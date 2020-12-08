import pytest

from feather_simple_api.resources.users.user import User
from feather_simple_api.resources.users.user_dto import UserDto
from .test_input import complete_data


@pytest.mark.unit
def test_new_user_model():
    user = User(**complete_data)

    assert user.email == complete_data["email"]
    assert user.firstname == complete_data["firstname"]
    assert user.address == complete_data["address"]
    assert user.occupation == complete_data["occupation"]
    assert user.has_child == complete_data["has_child"]
    assert user.child_num == complete_data["child_num"]


@pytest.mark.unit
def test_new_user_dto():
    user = UserDto(**complete_data)

    assert user.email == complete_data["email"]
    assert user.firstname == complete_data["firstname"]
    assert user.address == complete_data["address"]
    assert user.occupation == complete_data["occupation"]
    assert user.has_child == complete_data["has_child"]
    assert user.child_num == complete_data["child_num"]
