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


import date_pb2 as date__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11indications.proto\x12\x0bindications\x1a\ndate.proto\x1a\x1bgoogle/protobuf/empty.proto\"F\n\x15GetIndicationsRequest\x12\x18\n\x10indicationTypeID\x18\x01 \x01(\x05\x12\x13\n\x0bmaxQuantity\x18\x02 \x01(\x05\"s\n\x15PostIndicationRequest\x12\x19\n\x11indicationsTypeID\x18\x01 \x01(\x05\x12\x12\n\nindication\x18\x02 \x01(\x05\x12\x1d\n\tcreatedAt\x18\x03 \x01(\x0b\x32\x05.DateH\x00\x88\x01\x01\x42\x0c\n\n_createdAt\"`\n\nIndication\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nindication\x18\x02 \x01(\x05\x12\x18\n\x10indicationTypeID\x18\x03 \x01(\x05\x12\x18\n\tcreatedAt\x18\x04 \x01(\x0b\x32\x05.Date\"C\n\x13IndicationsResponse\x12,\n\x0bindications\x18\x01 \x03(\x0b\x32\x17.indications.Indication\"D\n\x1aGetIndicationsTypesRequest\x12\x11\n\taddressID\x18\x01 \x01(\x05\x12\x13\n\x0bmaxQuantity\x18\x02 \x01(\x05\"<\n\x19PostIndicationTypeRequest\x12\x11\n\taddressID\x18\x01 \x01(\x05\x12\x0c\n\x04type\x18\x02 \x01(\t\"=\n\x0eIndicationType\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x11\n\taddressID\x18\x02 \x01(\x05\x12\x0c\n\x04type\x18\x03 \x01(\t\"Q\n\x18IndicationsTypesResponse\x12\x35\n\x10indicationsTypes\x18\x01 \x03(\x0b\x32\x1b.indications.IndicationType2\xf8\x02\n\x0bIndications\x12N\n\x0ePostIndication\x12\".indications.PostIndicationRequest\x1a\x16.google.protobuf.Empty\"\x00\x12X\n\x0eGetIndications\x12\".indications.GetIndicationsRequest\x1a .indications.IndicationsResponse\"\x00\x12V\n\x12PostIndicationType\x12&.indications.PostIndicationTypeRequest\x1a\x16.google.protobuf.Empty\"\x00\x12g\n\x13GetIndicationsTypes\x12\'.indications.GetIndicationsTypesRequest\x1a%.indications.IndicationsTypesResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'indications_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETINDICATIONSREQUEST._serialized_start=75
  _GETINDICATIONSREQUEST._serialized_end=145
  _POSTINDICATIONREQUEST._serialized_start=147
  _POSTINDICATIONREQUEST._serialized_end=262
  _INDICATION._serialized_start=264
  _INDICATION._serialized_end=360
  _INDICATIONSRESPONSE._serialized_start=362
  _INDICATIONSRESPONSE._serialized_end=429
  _GETINDICATIONSTYPESREQUEST._serialized_start=431
  _GETINDICATIONSTYPESREQUEST._serialized_end=499
  _POSTINDICATIONTYPEREQUEST._serialized_start=501
  _POSTINDICATIONTYPEREQUEST._serialized_end=561
  _INDICATIONTYPE._serialized_start=563
  _INDICATIONTYPE._serialized_end=624
  _INDICATIONSTYPESRESPONSE._serialized_start=626
  _INDICATIONSTYPESRESPONSE._serialized_end=707
  _INDICATIONS._serialized_start=710
  _INDICATIONS._serialized_end=1086
# @@protoc_insertion_point(module_scope)
