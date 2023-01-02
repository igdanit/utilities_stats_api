import grpc
from datetime import datetime
from bson import objectid
from grpc.aio import ServicerContext
from grpcService.exceptions import BadRequest

import grpcService.protobufs.indications_pb2_grpc as indications_pb2_grpc
from grpcService.protobufs.indications_pb2 import GetIndicationsRequest, PostIndicationRequest, PostIndicationTypeRequest, GetIndicationsTypesRequest, Indication, IndicationsResponse, IndicationType, IndicationsTypesResponse
from motorService.motorClient import IndicationMongoService
from grpcService.protobufs.date_pb2 import Date
from google.protobuf.empty_pb2 import Empty
from motorService.serializer import grpcSerializer

from motorService.exceptions import IndexPairAlreadyExist


class IndicationsService(indications_pb2_grpc.IndicationsServicer):

    def __init__(self, database: IndicationMongoService, serializer: grpcSerializer) -> None:
        self._db = database
        self.serializer = serializer

    async def GetIndications(self, request: GetIndicationsRequest, context: ServicerContext):
        indications_list = await self._db.get_indications(
            {'indicationTypeID': request.indicationTypeID},
            request.maxQuantity
        )

        # passing to IndicationsRespose a generator obj
        return IndicationsResponse(indications=(
            Indication(
                # Convert ObjectID to hex string 
                id = str(indication['_id']),
                indication = indication['indication'],
                indicationTypeID = indication['indicationTypeID'],
                createdAt = Date(**indication['cretedAt'])
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

    async def PostIndication(self, request: PostIndicationRequest, context: ServicerContext):
        #Check correctness of
        # If date has default value then set date.now()
        if not (request.HasField('createdAt')):
            today = datetime.utcnow()
            request.createdAt = Date(
                day=today.day,
                month=today.month,
                year=today.year
                )

        serialized_indcation = self.serializer.serialize_indication(request)
        
        try:
            await self._db.insert_indication(serialized_indcation)
        except IndexPairAlreadyExist as e:
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details(e.msg)
        return Empty()

    async def getIndicationsTypes(self, request: GetIndicationsTypesRequest, context: ServicerContext):
        indication_types_list = await self._db.get_indication_types(
            {'addressID': request.addressID},
            request.maxQuantity
        )
        return IndicationsTypesResponse((
            IndicationType(
                # Convert ObjectID to hex string
                id=str(indication_type["_id"]),
                addressID=indication_type["addressID"],
                type=indication_type["type"]
            ) for indication_type in indication_types_list
        ))

    async def PostIndicationType(self, request: PostIndicationTypeRequest, context: ServicerContext):
        serialized_type = self.serializer.serialize_indication_type(request)

        try:
            await self._db.insert_indication_type(serialized_type)
        except IndexPairAlreadyExist as e:
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details(e.msg)
        return Empty()
