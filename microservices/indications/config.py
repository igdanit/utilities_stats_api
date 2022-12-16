from pydantic import BaseSettings

class Settings(BaseSettings):
    
    MONGO_INITDB_ROOT_USERNAME: str
    MONGO_INITDB_ROOT_PASSWORD: str
    MONGO_INITDB_DATABASE: str

    DATABASE_URL: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


settings = Settings()