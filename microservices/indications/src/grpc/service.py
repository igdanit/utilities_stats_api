from protobufs import indications_pb2_grpc
from protobufs.indications_pb2 import IndicationsRequest, IndicationsResponse
from motor.prisma import PrismaClient

class IndicationsService(indications_pb2_grpc.IndicationsServicer):

    def __init__(self) -> None:
        self.prisma = PrismaClient()        


    async def get_indications(self, request, context):
        pass

    async def post_indications(self, request, context):
        pass

    async def get_indications_types(self, request, context):
        pass

    async def post_indication_type(self, request, context):
        pass