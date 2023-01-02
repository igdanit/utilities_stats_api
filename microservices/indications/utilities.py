from motor.motor_asyncio import AsyncIOMotorCollection
from pymongo.errors import DuplicateKeyError

from motorService.exceptions import IndexPairAlreadyExist

from abc import ABC
from typing import Any, TypeVar
from loguru import logger

T = TypeVar("T")


""" Acts like ES6 Proxy object.
    Class successor should implement field that will intercepted.
    All intercepted field can whether invoke field of original object through self.target object """
class Proxy(ABC):
    def __init__(self, target: T) -> None:
        self.target: T = target

    def __getattribute__(self, __name: str) -> Any:
        # Check does object itself has that attrubute
        result = object.__getattribute__(self, '__dict__').get(__name)

        """ 
        Collection object do not impelement truth value testing or bool().
        Please compare with None instead
        """
        if result == None:
            # Check maybe do ancestors have that method/attribute
            try:
                result = super().__getattribute__(__name)
            except AttributeError:
                pass

        if result == None:
            # Get proxified object's property
            try:
                result = getattr(self.target, __name)
            except AttributeError:
                pass

        if result == None:
            raise AttributeError()
        return result


class MotorProxy(Proxy):
    def __init__(self, target: AsyncIOMotorCollection) -> None:
        super().__init__(target)

    async def insert_one(self, *args, **kwargs):
        try:
            await self.target.insert_one(*args, **kwargs)
        except DuplicateKeyError as e:
            raise IndexPairAlreadyExist(msg=e.error)
        except Exception as e:
            logger.error(e)
            raise e


def singleton(cls):
    instances = {}
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper
