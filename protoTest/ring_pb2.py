# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ring.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nring.proto\x12\x04Ring\"\x19\n\x08IDReqMsg\x12\r\n\x05token\x18\x01 \x01(\t\"B\n\x0cIDReqRespMsg\x12\x11\n\terrorCode\x18\x01 \x01(\x03\x12\x0f\n\x07\x61gentId\x18\x02 \x01(\t\x12\x0e\n\x06nodeId\x18\x03 \x01(\t2=\n\tNode2Node\x12\x30\n\x08obtainId\x12\x0e.Ring.IDReqMsg\x1a\x12.Ring.IDReqRespMsg\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ring_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _IDREQMSG._serialized_start=20
  _IDREQMSG._serialized_end=45
  _IDREQRESPMSG._serialized_start=47
  _IDREQRESPMSG._serialized_end=113
  _NODE2NODE._serialized_start=115
  _NODE2NODE._serialized_end=176
# @@protoc_insertion_point(module_scope)
