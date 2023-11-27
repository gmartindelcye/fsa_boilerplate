from pydantic import BaseSettings


class Settings(BaseSettings):
    # Base
    API_V1_PREFIX: str
    DEBUG: bool
    PROJECT_NAME: str
    VERSION: str
    DESCRIPTION: str

    # Database
    DB_ASYNC_CONNECTION_STR: str
    DB_ASYNC_TEST_CONNECTION_STR: str
    DB_EXCLUDE_TABLES: str

    # Environment
    ENV: str
    SECRET: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
