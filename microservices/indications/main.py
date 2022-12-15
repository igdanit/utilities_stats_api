import asyncio
import grpc
import grpc.aio

from grpcServer import indications_pb2_grpc
from grpcServer.service import IndicationsService

async def main():
    grpc.aio.init_grpc_aio()
    server = grpc.aio.server()
    server.add_insecure_port("[::]:50051")
    indications_pb2_grpc.add_IndicationsServicer_to_server(IndicationsService(), server)

    await server.start()
    await server.wait_for_termination()

if (__name__ == '__main__'):
    asyncio.run(main())