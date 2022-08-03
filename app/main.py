from fastapi import FastAPI, HTTPException, Request, status
from jose import JWTError, jwt
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.authentication import (
    AuthenticationBackend,
    AuthCredentials,
    UnauthenticatedUser,
)
from fastapi.security.utils import get_authorization_scheme_param

from .api import api_router
from .common.events import app_startup_event
from .common.settings import settings
from .models.auth import AuthenticatedUser


class AuthBackend(AuthenticationBackend):
    async def authenticate(self, request: Request):
        token = request.cookies.get("access_token")
        if not token:
            return (AuthCredentials(["anonymous"]), UnauthenticatedUser)

        _, param = get_authorization_scheme_param(token)
        try:
            payload = jwt.decode(param, settings.secret_key, algorithms=[settings.algorithm])
            auth_user = AuthenticatedUser(
                user_name=payload.get("sub"), rank=payload.get("rank")
            )
        except JWTError as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            ) from e
        return (AuthCredentials(["authenticated"]), auth_user)


server = FastAPI(
    title="FastAPI with ArangoDB",
    on_startup=[app_startup_event()],
    debug=settings.debug_mode,
)

server.include_router(api_router)
server.add_middleware(AuthenticationMiddleware, backend=AuthBackend())
