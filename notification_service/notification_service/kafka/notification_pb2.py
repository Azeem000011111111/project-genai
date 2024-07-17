# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: notification_pb2.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16notification_pb2.proto\x12\x14notification_service\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1bgoogle/protobuf/empty.proto\"z\n\x0cNotification\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"D\n\x12NotificationCreate\x12\x0f\n\x07user_id\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\"~\n\x10NotificationRead\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0f\n\x07user_id\x18\x02 \x01(\x05\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12.\n\ncreated_at\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"#\n\x15NotificationIdRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"g\n\x19NotificationUpdateRequest\x12\n\n\x02id\x18\x01 \x01(\x05\x12>\n\x0cnotification\x18\x02 \x01(\x0b\x32(.notification_service.NotificationCreate2\x89\x04\n\x13NotificationService\x12\x66\n\x12\x43reateNotification\x12(.notification_service.NotificationCreate\x1a&.notification_service.NotificationRead\x12T\n\x10GetNotifications\x12\x16.google.protobuf.Empty\x1a&.notification_service.NotificationRead0\x01\x12j\n\x13GetNotificationById\x12+.notification_service.NotificationIdRequest\x1a&.notification_service.NotificationRead\x12Y\n\x12\x44\x65leteNotification\x12+.notification_service.NotificationIdRequest\x1a\x16.google.protobuf.Empty\x12m\n\x12UpdateNotification\x12/.notification_service.NotificationUpdateRequest\x1a&.notification_service.NotificationReadb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'notification_pb2_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NOTIFICATION._serialized_start=110
  _NOTIFICATION._serialized_end=232
  _NOTIFICATIONCREATE._serialized_start=234
  _NOTIFICATIONCREATE._serialized_end=302
  _NOTIFICATIONREAD._serialized_start=304
  _NOTIFICATIONREAD._serialized_end=430
  _NOTIFICATIONIDREQUEST._serialized_start=432
  _NOTIFICATIONIDREQUEST._serialized_end=467
  _NOTIFICATIONUPDATEREQUEST._serialized_start=469
  _NOTIFICATIONUPDATEREQUEST._serialized_end=572
  _NOTIFICATIONSERVICE._serialized_start=575
  _NOTIFICATIONSERVICE._serialized_end=1096
# @@protoc_insertion_point(module_scope)