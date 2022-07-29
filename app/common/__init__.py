
import logging as log
import sys

from loguru import logger

from .logging import InterceptHandler
from .settings import settings


LOGGING_LEVEL = log.DEBUG if settings.debug_mode else log.INFO

log.basicConfig(
    handlers=[InterceptHandler(level=LOGGING_LEVEL)], level=LOGGING_LEVEL
)
logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])

