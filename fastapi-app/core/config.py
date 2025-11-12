from pydantic import BaseModel
from pydantic_settings import BaseSettings


class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8080
    username: str
    password: str


class ApiPrefix(BaseModel):
    api_prefix: str = "/api"


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db_url: str = "sqlite:///db.sqlite3"


settings = Settings()
