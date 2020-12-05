from flask_jwt_extended import create_access_token
from werkzeug.exceptions import UnprocessableEntity
from feather_simple_api.resources.users.users_dao import UserDao

from feather_simple_api.resources.users.user_dto import UserDto

from .security import encrypt_password, check_encrypted_password
from .auth_dto import AuthResponse
from .validators import AuthBody


class AuthService:
    def __init__(self, UserDao=UserDao):
        self.users_dao = UserDao()

    def signup(self, params: AuthBody) -> AuthResponse:
        params.password = encrypt_password(password=params.password)
        user_dto = UserDto.from_auth_body(auth_body=params)
        user = self.users_dao.create(params=user_dto)
        auth_response = AuthResponse(
            access_token=create_access_token(identity=user.id), user=user
        )

        return auth_response

    def login(self, params: AuthBody) -> AuthResponse:
        user = self.users_dao.get_by_email(params.email)

        if not user:
            raise UnprocessableEntity("Invalid email and/or password")

        if not check_encrypted_password(params.password, user.password):
            raise UnprocessableEntity("Invalid email and/or password")

        auth_response = AuthResponse(
            access_token=create_access_token(identity=user.id), user=user
        )

        return auth_response
