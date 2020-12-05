from flask_jwt_extended import JWTManager
from flask import Flask


def create_jwt_app(app: Flask) -> JWTManager:

    return JWTManager(app)
