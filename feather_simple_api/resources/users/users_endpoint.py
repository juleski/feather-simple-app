from flask import Blueprint
from flask_pydantic import validate

from .validators import UserBody
from .users_service import UsersService
from feather_simple_api.constants import EXCLUDE_KEYS

service = UsersService()

blueprint = Blueprint("users_endpoint", __name__)


@blueprint.route("/", methods=["POST"])
@validate()
def create(body: UserBody):
    response = service.create(params=body)

    return response.dict(exclude=EXCLUDE_KEYS), 201
