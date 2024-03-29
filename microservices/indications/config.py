from pydantic import BaseSettings
import os


class Settings(BaseSettings):

    MONGO_INITDB_ROOT_USERNAME: str
    MONGO_INITDB_ROOT_PASSWORD: str
    MONGO_INITDB_DATABASE: str

    DATABASE_URL: str
    MAX_DB_ENTRY: int

    TEST_DATABASE_URL: str
    TEST_GRPC_SERVICE_URL: str

    INDICATIONS_GRPC_SERVICE_URI: str

    class Config:
        env_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env") 
        env_file_encoding = "utf-8"


settings = Settings()