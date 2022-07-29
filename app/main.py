from fastapi import FastAPI
from app.config.events import app_startup_event
from .api import api_router

server = FastAPI(
    title="FastAPI with ArangoDB",
    on_startup=[app_startup_event()],
    debug=True
)

server.include_router(api_router)