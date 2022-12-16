import grpcServer.date_pb2 as _date_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteIndicationTypeRequest(_message.Message):
    __slots__ = ["IndicationTypeID"]
    INDICATIONTYPEID_FIELD_NUMBER: _ClassVar[int]
    IndicationTypeID: int
    def __init__(self, IndicationTypeID: _Optional[int] = ...) -> None: ...

class GetIndicationsRequest(_message.Message):
    __slots__ = ["indicationTypeID", "maxQuantity"]
    INDICATIONTYPEID_FIELD_NUMBER: _ClassVar[int]
    MAXQUANTITY_FIELD_NUMBER: _ClassVar[int]
    indicationTypeID: int
    maxQuantity: int
    def __init__(self, indicationTypeID: _Optional[int] = ..., maxQuantity: _Optional[int] = ...) -> None: ...

class GetIndicationsTypesRequest(_message.Message):
    __slots__ = ["addressID", "maxQuantity"]
    ADDRESSID_FIELD_NUMBER: _ClassVar[int]
    MAXQUANTITY_FIELD_NUMBER: _ClassVar[int]
    addressID: int
    maxQuantity: int
    def __init__(self, addressID: _Optional[int] = ..., maxQuantity: _Optional[int] = ...) -> None: ...

class Indication(_message.Message):
    __slots__ = ["createdAt", "id", "indication", "indicationTypeID"]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    INDICATIONTYPEID_FIELD_NUMBER: _ClassVar[int]
    INDICATION_FIELD_NUMBER: _ClassVar[int]
    createdAt: _date_pb2.Date
    id: int
    indication: int
    indicationTypeID: int
    def __init__(self, id: _Optional[int] = ..., indication: _Optional[int] = ..., indicationTypeID: _Optional[int] = ..., createdAt: _Optional[_Union[_date_pb2.Date, _Mapping]] = ...) -> None: ...

class IndicationType(_message.Message):
    __slots__ = ["addressID", "id", "type"]
    ADDRESSID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    addressID: int
    id: int
    type: str
    def __init__(self, id: _Optional[int] = ..., addressID: _Optional[int] = ..., type: _Optional[str] = ...) -> None: ...

class IndicationsResponse(_message.Message):
    __slots__ = ["indications"]
    INDICATIONS_FIELD_NUMBER: _ClassVar[int]
    indications: _containers.RepeatedCompositeFieldContainer[Indication]
    def __init__(self, indications: _Optional[_Iterable[_Union[Indication, _Mapping]]] = ...) -> None: ...

class IndicationsTypesResponse(_message.Message):
    __slots__ = ["indicationsTypes"]
    INDICATIONSTYPES_FIELD_NUMBER: _ClassVar[int]
    indicationsTypes: _containers.RepeatedCompositeFieldContainer[IndicationType]
    def __init__(self, indicationsTypes: _Optional[_Iterable[_Union[IndicationType, _Mapping]]] = ...) -> None: ...

class PostIndicationRequest(_message.Message):
    __slots__ = ["createdAt", "indication", "indicationsTypeID"]
    CREATEDAT_FIELD_NUMBER: _ClassVar[int]
    INDICATIONSTYPEID_FIELD_NUMBER: _ClassVar[int]
    INDICATION_FIELD_NUMBER: _ClassVar[int]
    createdAt: _date_pb2.Date
    indication: int
    indicationsTypeID: int
    def __init__(self, indicationsTypeID: _Optional[int] = ..., indication: _Optional[int] = ..., createdAt: _Optional[_Union[_date_pb2.Date, _Mapping]] = ...) -> None: ...

class PostIndicationTypeRequest(_message.Message):
    __slots__ = ["addressID", "type"]
    ADDRESSID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    addressID: int
    type: str
    def __init__(self, addressID: _Optional[int] = ..., type: _Optional[str] = ...) -> None: ...
