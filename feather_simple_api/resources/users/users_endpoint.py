from flask import Blueprint
from flask_pydantic import validate
from flask_jwt_extended import jwt_required, get_jwt_identity

from .validators import UserBody
from .users_service import UsersService
from feather_simple_api.constants import AUTH_EXCLUDE_KEYS, PROVIDER_EXCLUDE_KEYS

service = UsersService()

blueprint = Blueprint("users_endpoint", __name__)


@blueprint.route("/", methods=["POST"])
@validate()
def create(body: UserBody):
    response = service.create(params=body)

    return response.dict(exclude=AUTH_EXCLUDE_KEYS), 201


@blueprint.route("/recommendations", methods=["GET"])
@jwt_required
def get_recommendations():
    results = service.get_recommendations(user_id=get_jwt_identity())
    recommendations = [result.dict(exclude=PROVIDER_EXCLUDE_KEYS) for result in results]

    return {"recommendations": recommendations}, 200
