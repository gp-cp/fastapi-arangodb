from typing import Tuple
from fastapi import Depends
from ..config.exceptions import DocumentNotFoundError
from ..models.user import User, UserWithCredentials
from ..repository.user import UserRepo


class UserService:
    def __init__(self, repo: UserRepo = Depends()):
        self.repo = repo

    def get_by_key(self, key: str) -> Tuple[UserWithCredentials, DocumentNotFoundError]:
        try:
            user = self.repo.find_by_key(key)
        except DocumentNotFoundError as e:
            return None, e
        return UserWithCredentials(**user), None

    def create(self, user: User) -> UserWithCredentials:
        new_user = self.repo.insert(user.dict(by_alias=True))
        return UserWithCredentials(**new_user)
