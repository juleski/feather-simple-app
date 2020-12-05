from pydantic import BaseModel


class AuthBody(BaseModel):
    email: str
    password: str
