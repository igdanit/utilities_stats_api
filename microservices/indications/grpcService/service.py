import grpc
from datetime import datetime
from grpc.aio import ServicerContext

import grpcService.protobufs.indications_pb2_grpc as indications_pb2_grpc
from grpcService.protobufs.indications_pb2 import (
    GetIndicationsRequest,
    IsUsersIndicationRequest,
    IsUsersIndicationResponse,
    IsUsersIndicationTypeRequest,
    IsUsersIndicationTypeResponse,
    PostIndicationRequest,
    PostIndicationTypeRequest,
    GetIndicationsTypesRequest,
    Indication,
    IndicationsResponse,
    IndicationType,
    IndicationsTypesResponse,
)
from motorService.motorClient import IndicationMongoService
from grpcService.protobufs.date_pb2 import Date
from google.protobuf.empty_pb2 import Empty
from motorService.serializer import grpcSerializer

from motorService.exceptions import IndexPairAlreadyExist


class IndicationsService(indications_pb2_grpc.IndicationsServicer):
    def __init__(
        self, database: IndicationMongoService, serializer: grpcSerializer
    ) -> None:
        self._db = database
        self.serializer = serializer

    async def GetIndications(
        self, request: GetIndicationsRequest, context: ServicerContext
    ):
        indications_list = await self._db.get_indications(
            {"indicationsTypeID": request.indicationTypeID}, request.maxQuantity
        )
        # If there is no appropriate data
        if len(indications_list) == 0:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(
                f"There's no data such as indicationTypeID={request.indicationTypeID}"
            )

        # passing to IndicationsRespose a generator obj
        return IndicationsResponse(
            indications=(
                Indication(
                    # Convert ObjectID to hex string
                    id=str(indication["_id"]),
                    indication=indication["indication"],
                    indicationTypeID=indication["indicationsTypeID"],
                    userID=indication["userID"],
                    createdAt=Date(**indication["createdAt"]),
                )
                for indication in indications_list
            )
        )

    async def PostIndication(
        self, request: PostIndicationRequest, context: ServicerContext
    ):

        print(request)
        # If date has default value then set date.now()
        if not (request.HasField("createdAt")):
            today = datetime.utcnow()
            request.createdAt = Date(day=today.day, month=today.month, year=today.year)

        serialized_indcation = self.serializer.serialize_indication(request)

        try:
            await self._db.insert_indication(serialized_indcation)
        except IndexPairAlreadyExist as e:
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details(e.msg)
        return Empty()

    async def GetIndicationsTypes(
        self, request: GetIndicationsTypesRequest, context: ServicerContext
    ):
        indication_types_list = await self._db.get_indication_types(
            {"addressID": request.addressID}, request.maxQuantity
        )

        # If there is no appropriate data
        if len(indication_types_list) == 0:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details(
                f"There's no data such as addressID={request.addressID}"
            )

        return IndicationsTypesResponse(
            indicationsTypes=(
                IndicationType(
                    # Convert ObjectID to hex string
                    id=str(indication_type["_id"]),
                    addressID=indication_type["addressID"],
                    type=indication_type["type"],
                    userID=indication_type["userID"],
                )
                for indication_type in indication_types_list
            )
        )

    async def PostIndicationType(
        self, request: PostIndicationTypeRequest, context: ServicerContext
    ):
        serialized_type = self.serializer.serialize_indication_type(request)

        try:
            await self._db.insert_indication_type(serialized_type)
        except IndexPairAlreadyExist as e:
            context.set_code(grpc.StatusCode.ALREADY_EXISTS)
            context.set_details(e.msg)
        return Empty()

    async def IsUsersIndicationType(self, request: IsUsersIndicationTypeRequest, context: ServicerContext) -> IsUsersIndicationTypeResponse:
       query = {
        "_id": request.typeID, 
        "userID": request.userID,
       }
       indication_type = await self._db.get_one_indication_type(query)
       return IsUsersIndicationTypeResponse(
        status=indication_type is not None
        )

    async def IsUsersIndication(self, request: IsUsersIndicationRequest, context: ServicerContext) -> IsUsersIndicationResponse:
        query = {
            "_id": request.indicationID,
            "userID": request.userID,
        }
        indication = await self._db.get_one_indication(query)
        return IsUsersIndicationResponse(
            status=indication is not None
        )