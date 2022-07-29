from fastapi import FastAPI
from .common.events import app_startup_event
from .common.settings import settings
from .api import api_router

server = FastAPI(
    title="FastAPI with ArangoDB",
    on_startup=[app_startup_event()],
    debug=settings.debug_mode
)

server.include_router(api_router)