from typing import List
from fastapi import Depends
from app.models.user import User, UserInDB
from app.repository.user import UserRepo


class UserService:
    def __init__(self, repo: UserRepo = Depends()):
        self.repo = repo

    def create(self, user: User) -> UserInDB:
        

        new_user = self.repo.insert(user.dict(by_alias=True))
        return UserInDB(**new_user)
