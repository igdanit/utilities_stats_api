import motor.motor_asyncio as motor
from src.config import settings
from abc import ABC, abstractmethod

def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

class MotorClient(ABC):

    def __init__(self, uri: str, db_name: str) -> None:
        pass

    @abstractmethod
    def get_collection(self, collection_name: str):
        pass

    @abstractmethod
    def create_collection(self, collection_name: str):
        pass

    @abstractmethod
    def create_document(self, document):
        pass

    @abstractmethod
    def edit_document(self):
        pass

    @abstractmethod
    def delete_document(self):
        pass

    @abstractmethod
    def delete_collection(self):
        pass

@singleton
class MongoClient(MotorClient):

    def __init__(self, uri=settings.DATABASE_URL, db_name=settings.MONGO_INITDB_DATABASE):
        self._client = motor.AsyncIOMotorClient(uri)
        self.db = self._client[db_name]

    def get_collection(self, collection_name: str):
        return self.db[collection_name]


class IndicationService:

    def __init__(self, client_class):
        self._client = client_class()

    def get_indication(self):
        self._client


