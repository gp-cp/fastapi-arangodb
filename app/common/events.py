from .database import connect_database, create_collections

def app_startup_event():
    async def start_app() -> None:
        connect_database()
        create_collections()

    return start_app