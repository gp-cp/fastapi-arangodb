from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

from .user import router as user_router

api_router = APIRouter(default_response_class=ORJSONResponse, prefix="/api")

api_router.include_router(user_router)