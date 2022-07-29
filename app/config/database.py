from arango import ArangoClient
from arango.database import StandardDatabase
from loguru import logger


from .config import settings
from orjson import dumps, loads

# Initialize the ArangoDB client.
class ArangoDB:
    client: StandardDatabase


db = ArangoDB()


def connect_database():
    client = ArangoClient(
        hosts=settings.arango_host, serializer=dumps, deserializer=loads
    )
    sys_db = client.db(
        "_system", username="root", password=settings.arango_root_password
    )

    user_exists = sys_db.has_user(settings.arango_user)
    if not user_exists:
        sys_db.create_user(settings.arango_user, settings.arango_password)

    db_exists = sys_db.has_database(settings.arango_db)
    if not db_exists:
        sys_db.create_database(settings.arango_db)

    sys_db.update_permission(
        username=settings.arango_user, permission="rw", database=settings.arango_db
    )

    db.client = client.db(
        settings.arango_db,
        username=settings.arango_user,
        password=settings.arango_password,
    )


def create_collections():
    # TODO: Better place for collection list
    collections = ["users"]

    for c in collections:
        has_col = db.client.has_collection(c)
        if not has_col:
            db.client.create_collection(c)
