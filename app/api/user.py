from fastapi import APIRouter, Depends

from app.models.user import User
from app.services.user import UserService


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("")
async def create_user(user: User, user_service: UserService = Depends()):
    return user_service.create(user)