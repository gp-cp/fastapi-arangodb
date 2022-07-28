
from .base import BaseRepo


class UserRepo(BaseRepo):
    def __init__(self):
        super().__init__(collection="users")