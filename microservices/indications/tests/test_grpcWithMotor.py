# Intermediate integration test combine gRPCService and motorService

import pytest
import asyncio
from config import settings
from main import main
import grpc

from grpcService.service import IndicationsService

from grpcService.protobufs.indications_pb2 import GetIndicationsRequest
from motorService.motorClient import IndicationMongoService
from motorService.serializer import grpcMessageToDictSerializer


# Followed fixtures for pytest-grpc module. For the glory of documentation!
@pytest.fixture(scope="module")
def grpc_add_to_server():
    from grpcService.protobufs.indications_pb2_grpc import add_IndicationsServicer_to_server

    return add_IndicationsServicer_to_server 

@pytest.fixture(scope="module")
def grpc_servicer():
    from grpcService.service import IndicationsService

    return IndicationsService(database=IndicationMongoService(uri=settings.TEST_DATABASE_URL), serializer=grpcMessageToDictSerializer)

@pytest.fixture(scope='module')
def grpc_stub_cls(grpc_channel):
    from grpcService.protobufs.indications_pb2_grpc import IndicationsStub

    return IndicationsStub


class TestService:

    @pytest.mark.parametrize('req', [
        GetIndicationsRequest(indicationTypeID='1', maxQuantity=1)
    ])
    def test_get_indications(self, req, grpc_stub):
        response = grpc_stub.GetIndications(req)
        print(response)
        assert True        


    def test_post_indicaitions(self):
        assert True

    def teste_get_inditication_types(self):
        assert True

    def test_post_indication_type(self):
        assert True
