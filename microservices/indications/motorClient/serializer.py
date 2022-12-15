import sys

sys.path.append('..')

from grpc.date_pb2 import Date
from grpc.indications_pb2 import PostIndicationRequest, PostIndicationTypeRequest
from abc import ABC, abstractmethod

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

    def serialize_indication(self, document: PostIndicationRequest) -> dict:
        return {
            'indication': document.indication,
            'indicationTypeID': document.indicationsTypeID,
            'createdAt': self.serialize_date(document.createdAt)
        }

    def serialize_indication_type(self, document: PostIndicationTypeRequest) -> dict:
        return {
            'addressID': document["addressID"],
            'type': document["type"]
        }

    def serialize_date(self, date: Date) -> dict:
        return {
            'day': date.day,
            'month': date.month,
            'year': date.year
        }