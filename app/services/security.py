from datetime import timedelta, datetime
from typing import Dict, Tuple
from fastapi import Depends
from jose import  jwt
from datetime import timezone
from ..common.exceptions import AuthenticationError
from ..common.settings import settings
from ..models.auth import AuthModel
from .user import UserService


class SecurityService:
    def __init__(self, user_service: UserService = Depends()):
        self.user_service = user_service

    def __create_access_token(self, data: Dict, expires_delta: timedelta):
        to_encode = data.copy()

        expire = datetime.now(timezone.utc) + expires_delta

        to_encode.update({"exp": expire})
        return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)

    def login(
        self, auth_model: AuthModel
    ) -> Tuple[str, timedelta, AuthenticationError]:
        user, e = self.user_service.find_by_user_name(auth_model.user_name)
        # Check Credentials
        if e or user.password != auth_model.password:
            return None, None, AuthenticationError()

        access_token_expires = timedelta(minutes=120)
        return (
            self.__create_access_token(
                data={"sub": user.user_name, "rank": user.rank},
                expires_delta=access_token_expires,
            ),
            access_token_expires,
            None,
        )
