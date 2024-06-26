# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arm_authorizer_server/arm_authorizer_server.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1arm_authorizer_server/arm_authorizer_server.proto\x12 mavsdk.rpc.arm_authorizer_server\x1a\x14mavsdk_options.proto\"\"\n SubscribeArmAuthorizationRequest\"-\n\x18\x41rmAuthorizationResponse\x12\x11\n\tsystem_id\x18\x01 \x01(\r\"5\n\x1d\x41\x63\x63\x65ptArmAuthorizationRequest\x12\x14\n\x0cvalid_time_s\x18\x01 \x01(\x05\"\x83\x01\n\x1e\x41\x63\x63\x65ptArmAuthorizationResponse\x12\x61\n\x1c\x61rm_authorizer_server_result\x18\x01 \x01(\x0b\x32;.mavsdk.rpc.arm_authorizer_server.ArmAuthorizerServerResult\"\x8b\x01\n\x1dRejectArmAuthorizationRequest\x12\x13\n\x0btemporarily\x18\x01 \x01(\x08\x12\x41\n\x06reason\x18\x02 \x01(\x0e\x32\x31.mavsdk.rpc.arm_authorizer_server.RejectionReason\x12\x12\n\nextra_info\x18\x03 \x01(\x05\"\x83\x01\n\x1eRejectArmAuthorizationResponse\x12\x61\n\x1c\x61rm_authorizer_server_result\x18\x01 \x01(\x0b\x32;.mavsdk.rpc.arm_authorizer_server.ArmAuthorizerServerResult\"\xc8\x01\n\x19\x41rmAuthorizerServerResult\x12R\n\x06result\x18\x01 \x01(\x0e\x32\x42.mavsdk.rpc.arm_authorizer_server.ArmAuthorizerServerResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"C\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x11\n\rRESULT_FAILED\x10\x02*\xd7\x01\n\x0fRejectionReason\x12\x1c\n\x18REJECTION_REASON_GENERIC\x10\x00\x12\x19\n\x15REJECTION_REASON_NONE\x10\x01\x12%\n!REJECTION_REASON_INVALID_WAYPOINT\x10\x02\x12\x1c\n\x18REJECTION_REASON_TIMEOUT\x10\x03\x12$\n REJECTION_REASON_AIRSPACE_IN_USE\x10\x04\x12 \n\x1cREJECTION_REASON_BAD_WEATHER\x10\x05\x32\x8a\x04\n\x1a\x41rmAuthorizerServerService\x12\xa3\x01\n\x19SubscribeArmAuthorization\x12\x42.mavsdk.rpc.arm_authorizer_server.SubscribeArmAuthorizationRequest\x1a:.mavsdk.rpc.arm_authorizer_server.ArmAuthorizationResponse\"\x04\x80\xb5\x18\x00\x30\x01\x12\xa1\x01\n\x16\x41\x63\x63\x65ptArmAuthorization\x12?.mavsdk.rpc.arm_authorizer_server.AcceptArmAuthorizationRequest\x1a@.mavsdk.rpc.arm_authorizer_server.AcceptArmAuthorizationResponse\"\x04\x80\xb5\x18\x01\x12\xa1\x01\n\x16RejectArmAuthorization\x12?.mavsdk.rpc.arm_authorizer_server.RejectArmAuthorizationRequest\x1a@.mavsdk.rpc.arm_authorizer_server.RejectArmAuthorizationResponse\"\x04\x80\xb5\x18\x01\x42\x34\n\x18io.mavsdk.arm_authorizerB\x18\x41rmAuthorizerServerProtob\x06proto3')

_REJECTIONREASON = DESCRIPTOR.enum_types_by_name['RejectionReason']
RejectionReason = enum_type_wrapper.EnumTypeWrapper(_REJECTIONREASON)
REJECTION_REASON_GENERIC = 0
REJECTION_REASON_NONE = 1
REJECTION_REASON_INVALID_WAYPOINT = 2
REJECTION_REASON_TIMEOUT = 3
REJECTION_REASON_AIRSPACE_IN_USE = 4
REJECTION_REASON_BAD_WEATHER = 5


_SUBSCRIBEARMAUTHORIZATIONREQUEST = DESCRIPTOR.message_types_by_name['SubscribeArmAuthorizationRequest']
_ARMAUTHORIZATIONRESPONSE = DESCRIPTOR.message_types_by_name['ArmAuthorizationResponse']
_ACCEPTARMAUTHORIZATIONREQUEST = DESCRIPTOR.message_types_by_name['AcceptArmAuthorizationRequest']
_ACCEPTARMAUTHORIZATIONRESPONSE = DESCRIPTOR.message_types_by_name['AcceptArmAuthorizationResponse']
_REJECTARMAUTHORIZATIONREQUEST = DESCRIPTOR.message_types_by_name['RejectArmAuthorizationRequest']
_REJECTARMAUTHORIZATIONRESPONSE = DESCRIPTOR.message_types_by_name['RejectArmAuthorizationResponse']
_ARMAUTHORIZERSERVERRESULT = DESCRIPTOR.message_types_by_name['ArmAuthorizerServerResult']
_ARMAUTHORIZERSERVERRESULT_RESULT = _ARMAUTHORIZERSERVERRESULT.enum_types_by_name['Result']
SubscribeArmAuthorizationRequest = _reflection.GeneratedProtocolMessageType('SubscribeArmAuthorizationRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBEARMAUTHORIZATIONREQUEST,
  '__module__' : 'arm_authorizer_server.arm_authorizer_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.arm_authorizer_server.SubscribeArmAuthorizationRequest)
  })
_sym_db.RegisterMessage(SubscribeArmAuthorizationRequest)

ArmAuthorizationResponse = _reflection.GeneratedProtocolMessageType('ArmAuthorizationResponse', (_message.Message,), {
  'DESCRIPTOR' : _ARMAUTHORIZATIONRESPONSE,
  '__module__' : 'arm_authorizer_server.arm_authorizer_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.arm_authorizer_server.ArmAuthorizationResponse)
  })
_sym_db.RegisterMessage(ArmAuthorizationResponse)

AcceptArmAuthorizationRequest = _reflection.GeneratedProtocolMessageType('AcceptArmAuthorizationRequest', (_message.Message,), {
  'DESCRIPTOR' : _ACCEPTARMAUTHORIZATIONREQUEST,
  '__module__' : 'arm_authorizer_server.arm_authorizer_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.arm_authorizer_server.AcceptArmAuthorizationRequest)
  })
_sym_db.RegisterMessage(AcceptArmAuthorizationRequest)

AcceptArmAuthorizationResponse = _reflection.GeneratedProtocolMessageType('AcceptArmAuthorizationResponse', (_message.Message,), {
  'DESCRIPTOR' : _ACCEPTARMAUTHORIZATIONRESPONSE,
  '__module__' : 'arm_authorizer_server.arm_authorizer_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.arm_authorizer_server.AcceptArmAuthorizationResponse)
  })
_sym_db.RegisterMessage(AcceptArmAuthorizationResponse)

RejectArmAuthorizationRequest = _reflection.GeneratedProtocolMessageType('RejectArmAuthorizationRequest', (_message.Message,), {
  'DESCRIPTOR' : _REJECTARMAUTHORIZATIONREQUEST,
  '__module__' : 'arm_authorizer_server.arm_authorizer_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.arm_authorizer_server.RejectArmAuthorizationRequest)
  })
_sym_db.RegisterMessage(RejectArmAuthorizationRequest)

RejectArmAuthorizationResponse = _reflection.GeneratedProtocolMessageType('RejectArmAuthorizationResponse', (_message.Message,), {
  'DESCRIPTOR' : _REJECTARMAUTHORIZATIONRESPONSE,
  '__module__' : 'arm_authorizer_server.arm_authorizer_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.arm_authorizer_server.RejectArmAuthorizationResponse)
  })
_sym_db.RegisterMessage(RejectArmAuthorizationResponse)

ArmAuthorizerServerResult = _reflection.GeneratedProtocolMessageType('ArmAuthorizerServerResult', (_message.Message,), {
  'DESCRIPTOR' : _ARMAUTHORIZERSERVERRESULT,
  '__module__' : 'arm_authorizer_server.arm_authorizer_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.arm_authorizer_server.ArmAuthorizerServerResult)
  })
_sym_db.RegisterMessage(ArmAuthorizerServerResult)

_ARMAUTHORIZERSERVERSERVICE = DESCRIPTOR.services_by_name['ArmAuthorizerServerService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030io.mavsdk.arm_authorizerB\030ArmAuthorizerServerProto'
  _ARMAUTHORIZERSERVERSERVICE.methods_by_name['SubscribeArmAuthorization']._options = None
  _ARMAUTHORIZERSERVERSERVICE.methods_by_name['SubscribeArmAuthorization']._serialized_options = b'\200\265\030\000'
  _ARMAUTHORIZERSERVERSERVICE.methods_by_name['AcceptArmAuthorization']._options = None
  _ARMAUTHORIZERSERVERSERVICE.methods_by_name['AcceptArmAuthorization']._serialized_options = b'\200\265\030\001'
  _ARMAUTHORIZERSERVERSERVICE.methods_by_name['RejectArmAuthorization']._options = None
  _ARMAUTHORIZERSERVERSERVICE.methods_by_name['RejectArmAuthorization']._serialized_options = b'\200\265\030\001'
  _REJECTIONREASON._serialized_start=861
  _REJECTIONREASON._serialized_end=1076
  _SUBSCRIBEARMAUTHORIZATIONREQUEST._serialized_start=109
  _SUBSCRIBEARMAUTHORIZATIONREQUEST._serialized_end=143
  _ARMAUTHORIZATIONRESPONSE._serialized_start=145
  _ARMAUTHORIZATIONRESPONSE._serialized_end=190
  _ACCEPTARMAUTHORIZATIONREQUEST._serialized_start=192
  _ACCEPTARMAUTHORIZATIONREQUEST._serialized_end=245
  _ACCEPTARMAUTHORIZATIONRESPONSE._serialized_start=248
  _ACCEPTARMAUTHORIZATIONRESPONSE._serialized_end=379
  _REJECTARMAUTHORIZATIONREQUEST._serialized_start=382
  _REJECTARMAUTHORIZATIONREQUEST._serialized_end=521
  _REJECTARMAUTHORIZATIONRESPONSE._serialized_start=524
  _REJECTARMAUTHORIZATIONRESPONSE._serialized_end=655
  _ARMAUTHORIZERSERVERRESULT._serialized_start=658
  _ARMAUTHORIZERSERVERRESULT._serialized_end=858
  _ARMAUTHORIZERSERVERRESULT_RESULT._serialized_start=791
  _ARMAUTHORIZERSERVERRESULT_RESULT._serialized_end=858
  _ARMAUTHORIZERSERVERSERVICE._serialized_start=1079
  _ARMAUTHORIZERSERVERSERVICE._serialized_end=1601
# @@protoc_insertion_point(module_scope)
