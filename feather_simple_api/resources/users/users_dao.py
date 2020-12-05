from typing import Optional

from werkzeug.exceptions import UnprocessableEntity
from feather_simple_api import db

from sqlalchemy import exc

from .user import User
from .user_dto import UserDto


class UserDao:
    def create(self, params: UserDto) -> UserDto:
        try:
            user = User(**params.dict())
            db.session.add(user)
            db.session.commit()

            return UserDto.from_orm(user)
        except exc.IntegrityError:
            raise UnprocessableEntity("Email already exists")

    def get_by_email(self, email: str) -> Optional[UserDto]:
        user = User.query.filter_by(email=email).first()

        if not user:
            return None

        return UserDto.from_orm(user)
