from feather_simple_api.resources.users.users_dao import UsersDao

from .questionnaire_dao import QuestionnairesDao
from .questionnaire_dto import QuestionnaireDto
from .validators import QuestionnaireBody


class QuestionnairesService:
    def __init__(self, QuestionnairesDao=QuestionnairesDao, UsersDao=UsersDao):
        self.questionnaires_dao = QuestionnairesDao()
        self.users_dao = UsersDao()

    def create(self, user_id: str, params: QuestionnaireBody) -> QuestionnaireDto:
        q_params = params.dict()
        q_params["user"] = user_id
        questionnaire_dto = QuestionnaireDto(**q_params)
        questionnaire = self.questionnaires_dao.create(params=questionnaire_dto)

        return questionnaire
