import pytest

from motorService.serializer import grpcMessageToDictSerializer as gRPCserializer

from grpcService.protobufs.indications_pb2 import (
    PostIndicationTypeRequest,
    PostIndicationRequest,
)
from grpcService.protobufs.date_pb2 import Date


@pytest.mark.parametrize(
    "date_object",
    [
        Date(day=1, month=1, year=1970),
    ],
)
def test_serialize_date(date_object):
    assert gRPCserializer.serialize_date(date_object) == {
        "day": 1,
        "month": 1,
        "year": 1970,
    }


@pytest.mark.parametrize(
    "indication_type",
    [
        PostIndicationTypeRequest(addressID=1, type="AMOGUS"),
    ],
)
def test_serialize_indication_type(indication_type: PostIndicationTypeRequest):
    assert gRPCserializer.serialize_indication_type(indication_type) == {
        "addressID": indication_type.addressID,
        "type": indication_type.type,
    }


@pytest.mark.parametrize(
    "indication",
    [
        PostIndicationRequest(
            indication=1,
            indicationsTypeID="1",
            createdAt=Date(day=1, month=1, year=1970),
        ),
    ],
)
def test_serialize_indication(indication: PostIndicationRequest):
    assert gRPCserializer.serialize_indication(indication) == {
        "indication": indication.indication,
        "indicationsTypeID": indication.indicationsTypeID,
        "createdAt": {
            "day": indication.createdAt.day,
            "month": indication.createdAt.month,
            "year": indication.createdAt.year,
        },
    }
