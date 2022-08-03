from pydantic import BaseModel

class AuthModel(BaseModel):
    user_name: str
    password: str


class AuthenticatedUser(BaseModel):
    user_name: str
    rank: str