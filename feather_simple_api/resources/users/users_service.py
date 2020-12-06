from flask_jwt_extended import create_access_token

from feather_simple_api.resources.auth.auth_dto import AuthResponse

from .users_dao import UserDao
from .user_dto import UserDto
from .validators import UserBody


class UsersService:
    def __init__(self, UserDao=UserDao):
        self.users_dao = UserDao()

    def create(self, params: UserBody) -> AuthResponse:
        user_dto = UserDto(**params.dict())
        user = self.users_dao.create(params=user_dto)
        auth_response = AuthResponse(
            access_token=create_access_token(identity=user.id), user=user
        )

        return auth_response
