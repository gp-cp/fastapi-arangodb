from pydantic import UUID5, BaseModel, Field
from uuid import uuid5, NAMESPACE_DNS
from ..common.settings import settings

def generate_id():
    return uuid5(NAMESPACE_DNS, settings.app_name)

class Base(BaseModel):
    id: str = Field(None,  alias="_id")
    key: UUID5 = Field(default_factory=generate_id, alias="_key")