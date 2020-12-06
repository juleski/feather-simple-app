from typing import List

from sqlalchemy.sql.elements import BinaryExpression
from feather_simple_api import db

from .provider import Provider
from .provider_dto import ProviderDto


class ProvidersDao:
    def get_providers(self, filter_exp: BinaryExpression) -> List[ProviderDto]:
        try:
            results = []
            resources = db.session.query(Provider).filter(*filter_exp).all()

            for resource in resources:
                results.append(ProviderDto.from_orm(resource))

            return results
        except Exception as e:
            raise e
