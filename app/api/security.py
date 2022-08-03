from fastapi import APIRouter, Depends, HTTPException, Response
from starlette.status import HTTP_401_UNAUTHORIZED
from ..services.security import SecurityService

from ..models.auth import AuthModel
from ..models.user import User


router = APIRouter(prefix="/auth", tags=["Security"])


@router.post("/login")
async def login(
    auth_model: AuthModel,
    response: Response,
    security_service: SecurityService = Depends(),
):

    token, expires, err = security_service.login(auth_model)
    
    if err:
        raise HTTPException(HTTP_401_UNAUTHORIZED, {"message": err.message})
    
    response.set_cookie(
        key="access_token",
        value=f"Bearer {token}",
        httponly=True,
        secure=True,
        max_age=expires.seconds,
    )

    return {"access_token": token, "token_type": "bearer"}
