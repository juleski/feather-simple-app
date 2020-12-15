from flask import Blueprint
from flask_pydantic import validate
from flask_jwt_extended import jwt_required, get_jwt_identity

from .validators import QuestionnaireBody
from .questionnaire_service import QuestionnairesService
from feather_simple_api.constants import AUTH_EXCLUDE_KEYS

service = QuestionnairesService()

blueprint = Blueprint("questionnaires_endpoint", __name__)


@blueprint.route("/", methods=["POST"])
@jwt_required
@validate()
def create(body: QuestionnaireBody):
    response = service.create(user_id=get_jwt_identity(), params=body)

    return response.dict(exclude=AUTH_EXCLUDE_KEYS), 201
