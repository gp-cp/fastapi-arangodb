
from typing import Dict, List
from ..common.exceptions import DocumentNotFoundError
from .base import BaseRepo


class UserRepo(BaseRepo):
    def __init__(self):
        super().__init__(collection="users")

    def find_by_user_name(self, user_name: str) -> List[Dict]:
        col = self.db.collection(self.collection)
        result = col.find({"user_name": user_name})
        if result.empty():
            raise DocumentNotFoundError(user_name)
        return list(result)