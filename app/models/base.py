from pydantic import UUID4, BaseModel, Field
from uuid import uuid4


class Base(BaseModel):
    id: str = Field(None,  alias="_id")
    key: UUID4 = Field(default_factory=uuid4, alias="_key")