from abc import ABC, abstractmethod
from grpcService.protobufs.date_pb2 import Date
from grpcService.protobufs.indications_pb2 import PostIndicationRequest, PostIndicationTypeRequest

class grpcSerializer(ABC):

    @abstractmethod
    def serialize_indication(self, document):
        pass

    @abstractmethod
    def serialize_indication_type(self, document):
        pass

    @abstractmethod
    def serialize_date(self, date):
        pass


class grpcMessageToDictSerializer(grpcSerializer):

    @classmethod
    def serialize_indication(cls, document: PostIndicationRequest) -> dict:
        return {
            'indication': document.indication,
            'indicationsTypeID': document.indicationsTypeID,
            'createdAt': cls.serialize_date(document.createdAt)
        }

    @classmethod
    def serialize_indication_type(cls, document: PostIndicationTypeRequest) -> dict:
        return {
            'addressID': document.addressID,
            'type': document.type,
        }

    @classmethod
    def serialize_date(cls, date: Date) -> dict:
        return {
            'day': date.day,
            'month': date.month,
            'year': date.year
        }
