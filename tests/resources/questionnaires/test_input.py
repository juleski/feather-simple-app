from feather_simple_api.resources.users.user import User

complete_data = {
    "email": "testing@email.com",
    "firstname": "test",
    "address": "Metro Manila",
    "occupation": "employed",
    "has_child": True,
    "child_num": 3,
}

user = User(
    email="user@test.com",
    firstname="test",
    address="test",
    occupation="employed",
    has_child=True,
    child_num=1,
)
