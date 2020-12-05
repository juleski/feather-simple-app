from pydantic import BaseModel, EmailStr
from datetime import datetime
from uuid import UUID
from typing import Optional

from feather_simple_api.resources.auth.validators import AuthBody


class UserDto(BaseModel):
    id: Optional[UUID]
    email: EmailStr
    password: str
    created: Optional[datetime]

    class Config:
        orm_mode = True

    @staticmethod
    def from_auth_body(auth_body: AuthBody):
        return UserDto(email=auth_body.email, password=auth_body.password)
