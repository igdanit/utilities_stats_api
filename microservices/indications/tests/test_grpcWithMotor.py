"""Intermediate integration test combine gRPCService and motorService"""

import pytest
from config import settings
import grpc
import datetime

from grpcService.service import IndicationsService
from grpcService.protobufs.indications_pb2_grpc import IndicationsStub
from grpcService.protobufs.indications_pb2 import GetIndicationsRequest, Indication, IndicationsResponse, IndicationType,IndicationsTypesResponse, GetIndicationsTypesRequest, PostIndicationRequest, PostIndicationTypeRequest
from grpcService.protobufs.date_pb2 import Date

from motorService.motorClient import IndicationMongoService
from motorService.serializer import grpcMessageToDictSerializer


@pytest.fixture(scope="module")
def grpc_stub():
    channel = grpc.insecure_channel(settings.TEST_GRPC_SERVICE_URL)
    stub = IndicationsStub(channel)
    yield stub

# Fetch known indicationTypeID. All settings and documents inserted to DB contains in ./dbSettings/initial_script.py
def get_mongodb_document(*, collection_name: str, query: dict) -> str:
    from pymongo import MongoClient
    client = MongoClient(settings.TEST_DATABASE_URL)
    db = client.get_database(settings.MONGO_INITDB_DATABASE)
    collection = db.get_collection(collection_name)
    query_result = collection.find_one(query)
    if not query_result: # Check is indications_type == None
        raise Exception(f"Document contained {query} don't exist in MongoDB ")
    return query_result

def known_indicationTypeID(*, query: dict):
    indication_type = get_mongodb_document(collection_name="indicationTypes", query=query)
    return str(indication_type['_id'])

def get_date_obj():
    today = datetime.datetime.today()
    return Date(day=today.day, month=today.month, year=today.year)


@pytest.mark.parametrize('req', [
    GetIndicationsRequest(indicationTypeID='1', maxQuantity=1),
    GetIndicationsRequest(indicationTypeID=known_indicationTypeID(query={"addressID": 1}), maxQuantity=1)    
])
def test_get_indications(req, grpc_stub: IndicationsStub):
    try:
        response: IndicationsResponse= grpc_stub.GetIndications(req)
        indication: Indication = response.indications[0] # pick first from list-like contrainer
        assert indication.indication == 1
    except grpc.RpcError as e:
        assert e.code() == grpc.StatusCode.NOT_FOUND

@pytest.mark.parametrize('req', [
    PostIndicationRequest(indicationsTypeID=known_indicationTypeID(query={"addressID": 1}), indication=314, createdAt=get_date_obj()),
    PostIndicationRequest(indicationsTypeID=known_indicationTypeID(query={"addressID": 1}), indication=314, createdAt=get_date_obj())
])
def test_post_indicaitions(req, grpc_stub: IndicationsStub):
    try:
        response = grpc_stub.PostIndication(req)
        assert response.code() == grpc.StatusCode.OK
    except grpc.RpcError as e:
        assert e.code() == grpc.StatusCode.UNKNOWN

@pytest.mark.parametrize('req', [

])
def teste_get_inditication_types(req, grpc_stub: IndicationsStub):
    assert True

@pytest.mark.parametrize('req', [

])
def test_post_indication_type(req, grpc_stub: IndicationsStub):
    assert True
