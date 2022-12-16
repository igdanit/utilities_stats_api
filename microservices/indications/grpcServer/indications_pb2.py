# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: indications.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import grpcServer.date_pb2 as date__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11indications.proto\x1a\ndate.proto\x1a\x1bgoogle/protobuf/empty.proto\"D\n\x1aGetIndicationsTypesRequest\x12\x11\n\taddressID\x18\x01 \x01(\x05\x12\x13\n\x0bmaxQuantity\x18\x02 \x01(\x05\"<\n\x19PostIndicationTypeRequest\x12\x11\n\taddressID\x18\x01 \x01(\x05\x12\x0c\n\x04type\x18\x02 \x01(\t\"7\n\x1b\x44\x65leteIndicationTypeRequest\x12\x18\n\x10IndicationTypeID\x18\x01 \x01(\x05\"=\n\x0eIndicationType\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\taddressID\x18\x02 \x01(\x05\x12\x0c\n\x04type\x18\x03 \x01(\t\"E\n\x18IndicationsTypesResponse\x12)\n\x10indicationsTypes\x18\x01 \x03(\x0b\x32\x0f.IndicationType\"F\n\x15GetIndicationsRequest\x12\x18\n\x10indicationTypeID\x18\x01 \x01(\x05\x12\x13\n\x0bmaxQuantity\x18\x02 \x01(\x05\"s\n\x15PostIndicationRequest\x12\x19\n\x11indicationsTypeID\x18\x01 \x01(\x05\x12\x12\n\nindication\x18\x02 \x01(\x05\x12\x1d\n\tcreatedAt\x18\x03 \x01(\x0b\x32\x05.DateH\x00\x88\x01\x01\x42\x0c\n\n_createdAt\"`\n\nIndication\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nindication\x18\x02 \x01(\x05\x12\x18\n\x10indicationTypeID\x18\x03 \x01(\x05\x12\x18\n\tcreatedAt\x18\x04 \x01(\x0b\x32\x05.Date\"7\n\x13IndicationsResponse\x12 \n\x0bindications\x18\x01 \x03(\x0b\x32\x0b.Indication2\xb6\x02\n\x0bIndications\x12\x44\n\x10post_indications\x12\x16.PostIndicationRequest\x1a\x16.google.protobuf.Empty\"\x00\x12\x41\n\x0fget_indications\x12\x16.GetIndicationsRequest\x1a\x14.IndicationsResponse\"\x00\x12L\n\x14post_indication_type\x12\x1a.PostIndicationTypeRequest\x1a\x16.google.protobuf.Empty\"\x00\x12P\n\x14get_indication_types\x12\x1b.GetIndicationsTypesRequest\x1a\x19.IndicationsTypesResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'indications_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETINDICATIONSTYPESREQUEST._serialized_start=62
  _GETINDICATIONSTYPESREQUEST._serialized_end=130
  _POSTINDICATIONTYPEREQUEST._serialized_start=132
  _POSTINDICATIONTYPEREQUEST._serialized_end=192
  _DELETEINDICATIONTYPEREQUEST._serialized_start=194
  _DELETEINDICATIONTYPEREQUEST._serialized_end=249
  _INDICATIONTYPE._serialized_start=251
  _INDICATIONTYPE._serialized_end=312
  _INDICATIONSTYPESRESPONSE._serialized_start=314
  _INDICATIONSTYPESRESPONSE._serialized_end=383
  _GETINDICATIONSREQUEST._serialized_start=385
  _GETINDICATIONSREQUEST._serialized_end=455
  _POSTINDICATIONREQUEST._serialized_start=457
  _POSTINDICATIONREQUEST._serialized_end=572
  _INDICATION._serialized_start=574
  _INDICATION._serialized_end=670
  _INDICATIONSRESPONSE._serialized_start=672
  _INDICATIONSRESPONSE._serialized_end=727
  _INDICATIONS._serialized_start=730
  _INDICATIONS._serialized_end=1040
# @@protoc_insertion_point(module_scope)
