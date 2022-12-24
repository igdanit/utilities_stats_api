# Intermediate integration test combine gRPCService and motorService

import pytest

from grpcService.service import IndicationsService
from motorService.motorClient import IndicationMongoService
from motorService.serializer import grpcMessageToDictSerializer

from grpcService.protobufs.indications_pb2 import GetIndicationsRequest


class TestService:

    service = IndicationsService(database=IndicationMongoService(), serializer=grpcMessageToDictSerializer())

    @pytest.mark.parametrize('req', [
        GetIndicationsRequest(indicationTypeID='1', maxQuantity=1)
    ])
    async def test_get_indications(self, req):
        response = await self.service.get_indications(req, None)
        print(response)
        assert True        


    async def test_post_indicaitions(self):
        assert True

    async def teste_get_inditication_types(self):
        assert True

    async def test_post_indication_type(self):
        assert True
