from feather_simple_api.resources.users.user import User


def test_new_user():

    user = User(email="test@test.com")
    assert user.email == "test@test.com"
