import motor.motor_asyncio as motor
from src.config import settings
from abc import ABC, abstractmethod
from typing import Dict, Awaitable, List
from datetime import datetime

from motor.motor_asyncio import AsyncIOMotorCollection

def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

# DB driver interface
class MotorClient(ABC):

    @abstractmethod
    def __init__(self, uri: str, db_name: str) -> None:
        pass

    @abstractmethod
    def get_collection(self, collection_name: str):
        pass

    @abstractmethod
    def delete_collection(self):
        pass

    @abstractmethod
    def serialize_document(self, document):
        pass


class MongoClient(MotorClient):

    # uri, db_name - forced keyword arguments
    def __init__(self, *,uri, db_name):
        self._client = motor.AsyncIOMotorClient(uri)
        self.db = self._client[db_name]

        # Some logs. % uri and db_name must not be available for all logs checkers %
        print(f'Connected to MongoDB by : {uri}')
        print(f'Connected to {db_name} database')

    # Return existing or creates new one
    def get_collection(self, collection_name) -> AsyncIOMotorCollection:
        return self.db[collection_name]


@singleton
class IndicationMongoService(MongoClient):

    def __init__(self, *args, **kwargs):

        if 'uri' not in kwargs:
            kwargs['uri'] = settings.DATABASE_URL
        if 'db_name' not in kwargs:
            kwargs['db_name'] = settings.MONGO_INITDB_DATABASE
        super().__init__(*args, **kwargs)

        # get collection or create new one
        self.indications = self.get_collection('indcations')
        self.indications_types= self.get_collection('indicationsTypes')

    async def insert_indication(self, indication):
        document = self.serialize_indication(indication)
        return await self.indications.insert_one(document)
    
    async def get_indications(self, query: Dict, amount: int) -> Awaitable[List]:
        cursor = self.indications.find(query)
        return await cursor.to_list(amount)

    async def insert_indication_type(self, type):
        document = self.serialize_indication_type(type)
        return await self.indications_types.insert_one(document)

    async def get_indications_types(self, query: Dict, amount: int):
        cursor = self.indications_types.find(query)
        return await cursor.to_list(amount)
        

    def serialize_indication(self, document) -> Dict:
        return {
            'indication': document["indications"],
            'indicationTypeID': document["indicationTypeID"],
            'createdAt': datetime.utcnow()
        }

    def serialize_indication_type(self, document) -> Dict:
        return {
            'userID': document["userID"],
            'addressID': document["addressID"],
            'type': document["type"]

        }

