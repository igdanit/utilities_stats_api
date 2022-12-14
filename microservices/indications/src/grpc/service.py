import sys

sys.path.append('..')

from grpc import ServicerContext
from protobufs import indications_pb2_grpc
from protobufs.indications_pb2 import GetIndicationsRequest, IndicationsResponse, Indication, PostIndicationRequest
from protobufs import Date

from motor import IndicationMongoService

class IndicationsService(indications_pb2_grpc.IndicationsServicer):

    def __init__(self, database: IndicationMongoService) -> None:
        self._db = database

    async def get_indications(self, request: GetIndicationsRequest, context: ServicerContext):
        indications_list = await self._db.get_indications(
            {'indicationTypeID': request.indicationsTypeID},
            request.maxQuantity
        )
        # return IndicationsResponse(map(
        #     lambda indication: Indication(
        #         id = indication._id,
        #         indication = indication.indication,
        #         indication_type = indication.indicationType,
        #         created_date = Date(**indication.cretedAt)
        #     ),
        #     indications_list
        #     ))

    async def post_indication(self, request: PostIndicationRequest, context: ServicerContext):
        self._db.insert_indication(request)

    async def get_indication_types(self, request, context: ServicerContext):
        indication_types_list = await self._db.get_indications_types(
            {'addressID': request.addressID},
            request.maxQuantity
        )

    async def post_indication_type(self, request, context: ServicerContext):
        self._db.insert_indication_type(request)