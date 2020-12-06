from typing import Optional

from feather_simple_api import db

from .user import User
from .user_dto import UserDto


class UsersDao:
    def create(self, params: UserDto) -> UserDto:
        user = User(**params.dict())
        db.session.add(user)
        db.session.commit()

        return UserDto.from_orm(user)

    def get_by_email(self, email: str) -> Optional[UserDto]:
        user = User.query.filter_by(email=email).first()

        if not user:
            return None

        return UserDto.from_orm(user)

    def get_by_id(self, id: str) -> Optional[UserDto]:
        user = User.query.filter_by(id=id).first()

        if not user:
            return None

        return UserDto.from_orm(user)
