from typing import List
from werkzeug.exceptions import UnprocessableEntity
from flask_jwt_extended import create_access_token

from feather_simple_api.resources.auth.auth_dto import AuthResponse
from feather_simple_api.resources.providers.providers_dao import ProvidersDao
from feather_simple_api.resources.providers.provider import Provider
from feather_simple_api.resources.providers.provider_dto import ProviderDto

from .users_dao import UsersDao
from .user_dto import UserDto
from .validators import UserBody


class UsersService:
    def __init__(self, UsersDao=UsersDao, ProvidersDao=ProvidersDao):
        self.users_dao = UsersDao()
        self.providers_dao = ProvidersDao()

    def create(self, params: UserBody) -> AuthResponse:
        user_dto = UserDto(**params.dict())
        user = self.users_dao.create(params=user_dto)
        auth_response = AuthResponse(
            access_token=create_access_token(identity=user.id), user=user
        )

        return auth_response

    def get_recommendations(self, user_id: str) -> List[ProviderDto]:
        user = self.users_dao.get_by_id(id=user_id)

        if not user:
            raise UnprocessableEntity("User does not exist")

        filter_exp = [(Provider.for_occupation == user.occupation)]
        if not user.has_child:
            filter_exp.append(Provider.price > 20)
        else:
            if user.child_num == 1:
                filter_exp.append(Provider.price > 20)

            elif user.child_num >= 2 and user.child_num <= 4:
                filter_exp.append(Provider.price < 20)
                filter_exp.append(Provider.price > 10)
            else:
                filter_exp.append(Provider.price < 10)

        results = self.providers_dao.get_providers(filter_exp)

        return results
