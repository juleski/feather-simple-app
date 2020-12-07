from uuid import uuid4

from feather_simple_api.resources.providers.provider import Provider
from feather_simple_api.resources.providers.provider_dto import ProviderDto
from feather_simple_api.resources.users.user import User
from feather_simple_api.resources.users.user_dto import UserDto


complete_data = {
    "email": "testing@email.com",
    "firstname": "test",
    "address": "Metro Manila",
    "occupation": "employed",
    "has_child": True,
    "child_num": 3,
}

data_without_email = complete_data.copy()
data_without_email.pop("email", None)

data_without_firstname = complete_data.copy()
data_without_firstname.pop("firstname", None)

data_without_address = complete_data.copy()
data_without_address.pop("address", None)

data_without_occupation = complete_data.copy()
data_without_occupation.pop("occupation", None)

data_without_has_child = complete_data.copy()
data_without_has_child.pop("has_child", None)
data_without_has_child.pop("child_num", None)

user = User(
    email="user@test.com",
    firstname="test",
    address="test",
    occupation="employed",
    has_child=True,
    child_num=1,
)

provider1 = Provider(
    name="Life Insurance",
    price=32.5,
    for_occupation=user.occupation,
    billing_period="monthly",
)

provider2 = Provider(
    name="Health Insurance",
    price=32.5,
    for_occupation=user.occupation,
)

user_dto = UserDto.from_orm(user)
user_dto.id = uuid4()

provider_dto = ProviderDto.from_orm(provider1)
