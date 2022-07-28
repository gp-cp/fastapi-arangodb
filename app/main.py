from fastapi import FastAPI
from app.config.events import app_startup_event


server = FastAPI(
    title="FastAPI with ArangoDB",
    on_startup=[app_startup_event()]
)
