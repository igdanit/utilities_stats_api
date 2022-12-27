import asyncio
import grpc
import grpc.aio

from grpcService.protobufs import indications_pb2_grpc
from grpcService.service import IndicationsService
from motorService.motorClient import IndicationMongoService
from motorService.serializer import grpcMessageToDictSerializer

import logger


async def main():
    grpc.aio.init_grpc_aio()
    server = grpc.aio.server()
    server.add_insecure_port("[::]:50051")
    db = IndicationMongoService()
    serializer = grpcMessageToDictSerializer
    indications_pb2_grpc.add_IndicationsServicer_to_server(IndicationsService(database=db, serializer=serializer), server)

    await server.start()
    await server.wait_for_termination()

if (__name__ == '__main__'):
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
