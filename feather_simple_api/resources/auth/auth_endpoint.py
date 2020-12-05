from flask import Blueprint, jsonify
from flask_pydantic import validate

from .validators import AuthBody
from .auth_service import AuthService

service = AuthService()

blueprint = Blueprint("auth_endpoint", __name__)


@blueprint.route("/signup", methods=["POST"])
@validate()
def signup(body: AuthBody):
    access_token = service.signup()

    return jsonify({"data": access_token})


@blueprint.route("/login", methods=["POST"])
@validate()
def login(body: AuthBody):
    access_token = service.signup()
    return jsonify({"data": access_token})
