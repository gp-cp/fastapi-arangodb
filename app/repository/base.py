from typing import Dict, List
from xmlrpc.client import Boolean
from ..common.database import db
from ..common.exceptions import DocumentNotFoundError


class BaseRepo:
    def __init__(self, *, collection: str):
        self.db = db.client
        self.collection = collection

    def get_all(self) -> List[Dict]:
        col = self.db.collection(self.collection)
        return col.all()

    def find_by_key(self, key: str) -> Dict:
        col = self.db.collection(self.collection)
        document = col.get(key)
        if not document:
            raise DocumentNotFoundError(key)
        return document

    def insert(self, document: Dict) -> Dict:
        result = self.db.insert_document(self.collection, document, return_new=True)
        return result["new"]

    def update(self, document: Dict) -> Dict:
        result = self.db.update_document(document, check_rev=True, return_new=True, sync=True)
        return result["new"]

    def delete(self, key: str):
        col = self.db.collection(self.collection)
        result = col.delete(key, sync=True, silent=True, ignore_missing=True)
        if not result:
           raise DocumentNotFoundError(key) 
