from arango.exceptions import DocumentUpdateError, DocumentInsertError
from typing import List, Tuple, Union
from fastapi import Depends
from pydantic import UUID4

from ..common.exceptions import DocumentNotFoundError
from ..models.user import User, UserModel, UserWithCredentials
from ..repository.user import UserRepo

class UserService:
    def __init__(self, repo: UserRepo = Depends()):
        self.repo = repo

    def get_all(self) -> List[UserWithCredentials]:
        users = self.repo.get_all()
        return [UserWithCredentials(**u) for u in users]

    def get_by_key(self, key: UUID4) -> Tuple[UserWithCredentials, DocumentNotFoundError]:
        try:
            user = self.repo.find_by_key(str(key))
        except DocumentNotFoundError as e:
            return None, e
        return UserWithCredentials(**user), None

    def create(self, user: UserModel) -> Tuple[UserWithCredentials, DocumentInsertError]:
        new_user = UserWithCredentials(**user.dict(), password="")
        try:
            new_user = self.repo.insert(new_user.dict(by_alias=True))
        except DocumentInsertError as e:
            return None, e
        return UserWithCredentials(**new_user), None

    def update(self, user: User) -> Tuple[UserWithCredentials, DocumentUpdateError]:
        try:
            updated_user = self.repo.update(user.dict(by_alias=True))
        except DocumentUpdateError as e:
            return None, e
        return UserWithCredentials(**updated_user), None

    def delete(self, key: UUID4) -> DocumentNotFoundError:
        try:
            self.repo.delete(str(key))
        except DocumentNotFoundError as e:
            return e
        return None

    def find_by_user_name(self, user_name: str):
        try:
            users = self.repo.find_by_user_name(user_name)
        except DocumentNotFoundError as e:
            return None, e
        # User name should be unique
        return UserWithCredentials(**users[0]), None