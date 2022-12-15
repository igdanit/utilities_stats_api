import sys
from datetime import datetime

sys.path.append('..')

from grpc import ServicerContext
import indications_pb2_grpc
from indications_pb2 import GetIndicationsRequest, PostIndicationRequest, PostIndicationTypeRequest, GetIndicationsTypesRequest, Indication, IndicationsResponse, IndicationType, IndicationsTypesResponse
from motorClient import IndicationMongoService
from date_pb2 import Date
from motorClient.serializer import grpcSerializer

class IndicationsService(indications_pb2_grpc.IndicationsServicer):

    def __init__(self, database: IndicationMongoService, serializer: grpcSerializer) -> None:
        self._db = database
        self.serializer = serializer

    async def get_indications(self, request: GetIndicationsRequest, context: ServicerContext):
        indications_list = await self._db.get_indications(
            {'indicationTypeID': request.indicationTypeID},
            request.maxQuantity
        )

        # passing to IndicationsRespose a generator obj
        return IndicationsResponse((
            Indication(
                id = int(indication['_id']),
                indication = int(indication['indication']),
                indicationTypeID = int(indication['indicationTypeID']),
                created_date = Date(**indication['cretedAt'])
            ) for indication in indications_list
        ))

        # return IndicationsResponse(map(
        #     lambda indication: Indication(
        #         id = int(indication['_id']),
        #         indication = int(indication['indication']),
        #         indicationTypeID = int(indication['indicationTypeID']),
        #         created_date = Date(**indication['cretedAt'])
        #         ),
        #         indications_list
        #     ))

    async def post_indication(self, request: PostIndicationRequest, context: ServicerContext):

        # If date has default value then set date.now()
        if not (request.HasField('createdAt')):
            today = datetime.utcnow()
            request["createdAt"] = {
                'day': today.day,
                'month': today.month,
                'year': today.year
                }

        serialized_indcation = self.serializer(request)
        await self._db.insert_indication(serialized_indcation)

    async def get_indication_types(self, request: GetIndicationsTypesRequest, context: ServicerContext):
        indication_types_list = await self._db.get_indications_types(
            {'addressID': request.addressID},
            request.maxQuantity
        )
        return IndicationsTypesResponse((
            IndicationType(
                id=int(indication_type["_id"]),
                addressID=int(indication_type["addressID"]),
                type=indication_type["type"]
            ) for indication_type in indication_types_list
        ))

    async def post_indication_type(self, request: PostIndicationTypeRequest, context: ServicerContext):
        serialized_type = self.serializer(request)
        await self._db.insert_indication_type(serialized_type)