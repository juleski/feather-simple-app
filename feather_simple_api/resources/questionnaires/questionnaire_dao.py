from typing import Optional

from feather_simple_api import db
from .questionnaire import Questionnaire
from .questionnaire_dto import QuestionnaireDto


class QuestionnairesDao:
    def create(self, params: QuestionnaireDto) -> QuestionnaireDto:
        questionnaire = Questionnaire(**params.dict())
        db.session.add(questionnaire)
        db.session.commit()

        return QuestionnaireDto.from_orm(questionnaire)

    def get_by_email(self, email: str) -> Optional[QuestionnaireDto]:
        questionnaire = Questionnaire.query.filter_by(email=email).first()

        if not questionnaire:
            return None

        return QuestionnaireDto.from_orm(questionnaire)

    def get_by_id(self, id: str) -> Optional[QuestionnaireDto]:
        questionnaire = Questionnaire.query.filter_by(id=id).first()

        if not questionnaire:
            return None

        return QuestionnaireDto.from_orm(questionnaire)
