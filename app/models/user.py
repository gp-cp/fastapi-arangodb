from enum import Enum
from pydantic import BaseModel, EmailStr
from .base import Base

class RankType(str, Enum):
    USR = "user"
    ADM = "admin"


class UserModel(BaseModel):
    user_name: str
    full_name: str
    email: EmailStr
    rank: RankType
    activated: bool = True


class User(Base, UserModel):
    pass


class UserWithCredentials(User):
    password: str = ""