from pydantic import BaseModel
from feather_simple_api.resources.users.user_dto import UserDto


class AuthResponse(BaseModel):
    access_token: str
    user: UserDto
