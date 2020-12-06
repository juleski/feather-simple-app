from pydantic import BaseModel, EmailStr, validator
from typing import Optional

from .enums import OccupationStatus


class UserBody(BaseModel):
    email: EmailStr
    firstname: str
    address: str
    occupation: OccupationStatus
    has_child: bool
    child_num: Optional[int]

    @validator("child_num", always=True)
    def validate_child_num(cls, v, values):
        if values.get("has_child", None):
            if v is None:
                raise ValueError("child_num field is requried when has_child is true")
            elif v <= 0:
                raise ValueError("child_num can not be less than 1")
        else:
            if v and v > 0:
                raise ValueError(
                    "child_num should not be set or set to 0, if has_child is false"
                )
        return v
