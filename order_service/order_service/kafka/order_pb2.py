# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: .proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x06.proto\x12\x05order\"1\n\tOrderItem\x12\x12\n\nproduct_id\x18\x01 \x01(\x05\x12\x10\n\x08quantity\x18\x02 \x01(\x05\"T\n\x0bOrderCreate\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x1f\n\x05items\x18\x02 \x03(\x0b\x32\x10.order.OrderItem\x12\x13\n\x0btotal_price\x18\x03 \x01(\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, '_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ORDERITEM._serialized_start=17
  _ORDERITEM._serialized_end=66
  _ORDERCREATE._serialized_start=68
  _ORDERCREATE._serialized_end=152
# @@protoc_insertion_point(module_scope)