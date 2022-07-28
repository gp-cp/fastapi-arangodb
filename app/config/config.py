from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    arango_host: str = Field(env="ARANGO_HOST", default="http://localhost:8529")
    arango_root_password: str = Field(env="ARANGO_ROOT_PASSWORD", default="uvaed5Qui3ea5ohd1ouneope")
    arango_password: str = Field(env="ARANGO_PASSWORD", default="arango")

    arango_user: str = Field(env="ARANGO_USER", default="arango")
    arango_db: str = Field(env="ARANGO_DB", default="api_db")


settings = Settings()