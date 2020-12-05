from pydantic import BaseModel, EmailStr


class AuthBody(BaseModel):
    email: EmailStr
    password: str
