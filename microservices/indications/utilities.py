from motor.motor_asyncio import AsyncIOMotorCollection
from pymongo.errors import DuplicateKeyError

from motorService.exceptions import IndexPairAlreadyExist

from abc import ABC
from typing import Any
from loguru import logger


# Acts like ES6 Proxy object
class Proxy(ABC):
    def __init__(self, target) -> None:
        self.target = target

    def __getattribute__(self, __name: str) -> Any:
        # Check does object itself has that attrubute
        result = object.__getattribute__(self, '__dict__').get(__name)

        """ 
        Collection object do not impelement truth value testing or bool().
        Please compare with None instead
        """
        if result == None:
            # Check maybe do ancestors have that method/attribute
            result = super().__getattribute__(__name)
        if result == None:
            raise AttributeError()
        return result


class MotorProxy(Proxy):
    def __init__(self, target: AsyncIOMotorCollection) -> None:
        super().__init__(target)

    async def insert_one(self, *args, **kwargs):
        try:
            await self.target.insert_one(*args, **kwargs)
        except DuplicateKeyError:
            raise IndexPairAlreadyExist()
        except Exception as e:
            logger.error(e)
            raise e
