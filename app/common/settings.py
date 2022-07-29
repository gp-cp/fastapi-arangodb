from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    app_name: str = Field(env="APP_NAME", default="FastApi-Arango")
    debug_mode: bool = Field(env="DEBUG_MODE", default=False)

    arango_host: str = Field(env="ARANGO_HOST", default="http://localhost:8529")
    arango_root_password: str = Field(env="ARANGO_ROOT_PASSWORD", default="MY_SUPER_HARD_PW")
    arango_password: str = Field(env="ARANGO_PASSWORD", default="arango")

    arango_user: str = Field(env="ARANGO_USER", default="arango")
    arango_db: str = Field(env="ARANGO_DB", default="api_db")



settings = Settings()