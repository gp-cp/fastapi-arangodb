from enum import Enum
from pydantic import EmailStr
from .base import Base

class RankType(str, Enum):
    USR = "user"
    ADM = "admin"


class User(Base):
    user_name: str
    full_name: str
    email: EmailStr
    rank: RankType
    activated: bool = True


class UserInDB(User):
    password: str = ""