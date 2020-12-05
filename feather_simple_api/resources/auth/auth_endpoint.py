from flask import Blueprint
from flask_pydantic import validate

from .validators import AuthBody
from .auth_service import AuthService
from .constants import EXCLUDE_KEYS

service = AuthService()

blueprint = Blueprint("auth_endpoint", __name__)


@blueprint.route("/signup", methods=["POST"])
@validate()
def signup(body: AuthBody):
    response = service.signup(params=body)

    return response.dict(exclude=EXCLUDE_KEYS)


@blueprint.route("/login", methods=["POST"])
@validate()
def login(body: AuthBody):
    response = service.login(params=body)

    return response.dict(exclude=EXCLUDE_KEYS)
