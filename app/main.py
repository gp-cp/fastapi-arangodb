from fastapi import FastAPI
from starlette.middleware.authentication import AuthenticationMiddleware

from .api import api_router
from .api.middlewares.authentication import AuthBackend
from .common.events import app_startup_event
from .common.settings import settings





server = FastAPI(
    title="FastAPI with ArangoDB",
    on_startup=[app_startup_event()],
    debug=settings.debug_mode,
)

server.include_router(api_router)
server.add_middleware(AuthenticationMiddleware, backend=AuthBackend())
