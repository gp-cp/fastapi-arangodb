from nanoid import generate
from pydantic import BaseModel, Field


class Base(BaseModel):
    id: str = Field(None,  alias="_id")
    key: str = Field(default_factory=generate, alias="_key")