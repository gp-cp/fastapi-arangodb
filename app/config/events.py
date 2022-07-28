from .database import connect_database

def app_startup_event():
    async def start_app() -> None:
        connect_database()

    return start_app