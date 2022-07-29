from typing import List
from fastapi import APIRouter, Depends, HTTPException
from fastapi.routing import JSONResponse
from starlette.status import HTTP_202_ACCEPTED, HTTP_404_NOT_FOUND
from pydantic import UUID4
from ..models.user import User, UserModel
from ..services.user import UserService


router = APIRouter(prefix="/users", tags=["Users"])


@router.get("", response_model=List[User], response_model_by_alias=True)
async def get_users(user_service: UserService = Depends()):
    return user_service.get_all()


@router.get("/{key}", response_model=User, response_model_by_alias=True)
async def get_user(key: UUID4, user_service: UserService = Depends()):
    user, err = user_service.get_by_key(key)
    if err:
        raise HTTPException(HTTP_404_NOT_FOUND, {"message": err.message})
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
        raise HTTPException(err.http_code, {"message": err.message})
    return result


@router.delete("/{key}")
async def delete_user(key: UUID4, user_service: UserService = Depends()):

    if err := user_service.delete(key):
        raise HTTPException(HTTP_404_NOT_FOUND, {"message": err.message})

    return JSONResponse(
        status_code=HTTP_202_ACCEPTED, content={"detail": "User deleted."}
    )
