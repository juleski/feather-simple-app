from pydantic import BaseModel, EmailStr
from datetime import datetime
from uuid import UUID
from typing import Optional


class QuestionnaireDto(BaseModel):
    id: Optional[UUID]
    email: EmailStr
    firstname: Optional[str]
    address: Optional[str]
    occupation: Optional[str]
    has_child: Optional[bool]
    child_num: Optional[int]
    user: Optional[UUID]
    created: Optional[datetime]

    class Config:
        orm_mode = True
