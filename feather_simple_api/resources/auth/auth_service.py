from flask_jwt_extended import create_access_token


class AuthService:
    def signup(self):
        access_token = create_access_token(identity="some-identiy")

        return access_token

    def login(self):
        access_token = create_access_token(identity="some-identiy")

        return access_token
