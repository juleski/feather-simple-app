from flask_jwt_extended import create_access_token
from werkzeug.exceptions import UnprocessableEntity
from feather_simple_api.resources.users.users_dao import UsersDao

from feather_simple_api.resources.users.user_dto import UserDto

from .security import encrypt_password, check_encrypted_password
from .auth_dto import AuthResponse
from .validators import AuthSignupBody, AuthLoginBody


class AuthService:
    def __init__(self, UsersDao=UsersDao):
        self.users_dao = UsersDao()

    def signup(self, params: AuthSignupBody) -> AuthResponse:
        params.password = encrypt_password(password=params.password)
        user_dto = UserDto(**params.dict())
        user = self.users_dao.create(params=user_dto)
        auth_response = AuthResponse(
            access_token=create_access_token(identity=user.id), user=user
        )

        return auth_response

    def login(self, params: AuthLoginBody) -> AuthResponse:
        user = self.users_dao.get_by_id(params.id)

        if not user:
            print("IN HERE")
            raise UnprocessableEntity("Invalid email and/or password")

        if not check_encrypted_password(params.password, user.password):
            raise UnprocessableEntity("Invalid email and/or password")

        auth_response = AuthResponse(
            access_token=create_access_token(identity=user.id), user=user
        )

        return auth_response
