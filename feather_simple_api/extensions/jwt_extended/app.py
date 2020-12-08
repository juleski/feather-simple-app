from flask_jwt_extended import JWTManager


def create_jwt_app() -> JWTManager:

    return JWTManager()
