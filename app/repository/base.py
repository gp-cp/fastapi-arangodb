from typing import Dict
from ..config.database import db
from ..config.exceptions import DocumentNotFoundError


class BaseRepo:
    def __init__(self, *, collection: str):
        self.db = db.client
        self.collection = collection

    def find_by_key(self, key: str) -> Dict:
        col = self.db.collection(self.collection)
        document = col.get(key)
        if not document:
            raise DocumentNotFoundError(key)
        return document

    def insert(self, document: Dict) -> Dict:
        result = self.db.insert_document(self.collection, document, return_new=True)
        return result["new"]