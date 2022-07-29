from typing import Dict, List, Union
from fastapi import APIRouter, Depends, HTTPException

from ..models.user import User, UserModel
from ..services.user import UserService


router = APIRouter(prefix="/users", tags=["Users"])

@router.get("", response_model=List[User], response_model_by_alias=True)
async def get_users(
    user_service: UserService = Depends()
):  
    return user_service.get_all()

@router.get("/{key}", response_model=User, response_model_by_alias=True)
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
    result, err = user_service.create(user)
    if err:
        raise HTTPException(err.http_code, {"message": err.message})
    return result

@router.put("", response_model=User, response_model_by_alias=True)
async def edit_user(user: User, user_service: UserService = Depends()):
    result, err = user_service.update(user)
    if err:
        raise HTTPException(err.error_code, {"message": err.message})
    return result