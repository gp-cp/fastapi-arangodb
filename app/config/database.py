from arango import ArangoClient
from arango.database import StandardDatabase


from .config import settings
from orjson import dumps, loads

# Initialize the ArangoDB client.
class ArangoDB:
    client: StandardDatabase

db = ArangoDB()


def connect_database():
    print("called")
    client = ArangoClient(hosts=settings.arango_host, serializer=dumps, deserializer=loads)
    sys_db = client.db("_system", username="root", password=settings.arango_root_password)
    
    db_exists = sys_db.has_database(settings.arango_db)
    if not db_exists:
        sys_db.create_database(settings.arango_db)

    db.client = client.db(settings.arango_db, username=settings.arango_user, password=settings.arango_password)
