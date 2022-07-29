from typing import Dict, Union
from fastapi import APIRouter, Depends, HTTPException

from ..models.user import User, UserModel
from ..services.user import UserService


router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/{id}", response_model=Union[User, Dict], response_model_by_alias=True)
async def get_user(
    key: str,
    user_service: UserService = Depends()
):  
    user, err = user_service.get_by_key(key)
    if err:
        raise HTTPException(404, {"message": err.message})
    return user


@router.post("", response_model=User, response_model_by_alias=True)
async def create_user(user: UserModel, user_service: UserService = Depends()):
    return user_service.create(user)