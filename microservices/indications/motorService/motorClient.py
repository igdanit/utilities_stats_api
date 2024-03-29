from abc import ABC, abstractmethod
from typing import Awaitable
from loguru import logger
from utilities import MotorProxy

from grpcService.protobufs.date_pb2 import Date
from grpcService.protobufs.indications_pb2 import (
    PostIndicationRequest,
    PostIndicationTypeRequest,
)
from motorService.exceptions import IndexPairAlreadyExist
from config import settings
from utilities import singleton

import motor.motor_asyncio as motor
from motor.motor_asyncio import AsyncIOMotorCollection
import pymongo.typings


# DB driver interface
class MotorClient(ABC):
    @abstractmethod
    def __init__(self, uri: str, db_name: str) -> None:
        pass

    @abstractmethod
    def get_collection(self, collection_name: str):
        pass


class MongoClient(MotorClient):

    # uri, db_name - forced keyword arguments
    def __init__(self, *, uri, db_name):
        self._client = motor.AsyncIOMotorClient(uri)
        self.db = self._client[db_name]

        # Some logs. % uri and db_name must not be available for all logs checkers %
        if (self._client.is_mongos):    # motor didn't implement __bool__, so need to compare with None etc.
            logger.info(f"Connected to MongoDB by : {uri}")
        else:
            logger.warning("MONGODB IS NOT AVAILABLE")

        if (self.db.name == db_name):
            logger.info(f"Connected to {db_name} database")

    def __enter__(self):
        return self

    # Close client connection
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._client.close
        logger.info("connection to MongoDB closed")

    # Return existing or creates new one
    def get_collection(self, collection_name) -> AsyncIOMotorCollection:
        return MotorProxy(self.db[collection_name])


@singleton
class IndicationMongoService(MongoClient):
    def __init__(self, *args, **kwargs):

        if "uri" not in kwargs:
            kwargs["uri"] = settings.TEST_DATABASE_URL
        if "db_name" not in kwargs:
            kwargs["db_name"] = settings.MONGO_INITDB_DATABASE
        super().__init__(*args, **kwargs)

        # get collection or create new one
        self.indications: AsyncIOMotorCollection = self.get_collection("indications")
        self.indications_types: AsyncIOMotorCollection = self.get_collection("indicationTypes")

    async def insert_indication(self, indication: dict):
        return await self.indications.insert_one(indication)

    async def get_indications(self, query: dict, amount: int) -> Awaitable[list]:
        cursor = self.indications.find(query)
        return await cursor.to_list(settings.MAX_DB_ENTRY if amount == 0 else amount)

    async def insert_indication_type(self, type: dict):
        return await self.indications_types.insert_one(type)

    async def get_indication_types(self, query: dict, amount: int) -> Awaitable[list]:
        cursor = self.indications_types.find(query)
        return await cursor.to_list(settings.MAX_DB_ENTRY if amount == 0 else amount)

    async def get_one_indication(self, query: dict) -> Awaitable[pymongo.typings._DocumentType | None]:
        return self.indications.find_one(query)

    async def get_one_indication_type(self, query: dict) -> Awaitable[pymongo.typings._DocumentType | None]:
        return self.indications_types.find_one(query)
