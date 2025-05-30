# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: gripper/gripper.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'gripper/gripper.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15gripper/gripper.proto\x12\x12mavsdk.rpc.gripper\"\x1f\n\x0bGrabRequest\x12\x10\n\x08instance\x18\x01 \x01(\r\"I\n\x0cGrabResponse\x12\x39\n\x0egripper_result\x18\x01 \x01(\x0b\x32!.mavsdk.rpc.gripper.GripperResult\"\"\n\x0eReleaseRequest\x12\x10\n\x08instance\x18\x01 \x01(\r\"L\n\x0fReleaseResponse\x12\x39\n\x0egripper_result\x18\x01 \x01(\x0b\x32!.mavsdk.rpc.gripper.GripperResult\"\xf6\x01\n\rGripperResult\x12\x38\n\x06result\x18\x01 \x01(\x0e\x32(.mavsdk.rpc.gripper.GripperResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\x96\x01\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x02\x12\x0f\n\x0bRESULT_BUSY\x10\x03\x12\x12\n\x0eRESULT_TIMEOUT\x10\x04\x12\x16\n\x12RESULT_UNSUPPORTED\x10\x05\x12\x11\n\rRESULT_FAILED\x10\x06*D\n\rGripperAction\x12\x1a\n\x16GRIPPER_ACTION_RELEASE\x10\x00\x12\x17\n\x13GRIPPER_ACTION_GRAB\x10\x01\x32\xb3\x01\n\x0eGripperService\x12K\n\x04Grab\x12\x1f.mavsdk.rpc.gripper.GrabRequest\x1a .mavsdk.rpc.gripper.GrabResponse\"\x00\x12T\n\x07Release\x12\".mavsdk.rpc.gripper.ReleaseRequest\x1a#.mavsdk.rpc.gripper.ReleaseResponse\"\x00\x42!\n\x11io.mavsdk.gripperB\x0cGripperProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'gripper.gripper_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021io.mavsdk.gripperB\014GripperProto'
  _globals['_GRIPPERACTION']._serialized_start=516
  _globals['_GRIPPERACTION']._serialized_end=584
  _globals['_GRABREQUEST']._serialized_start=45
  _globals['_GRABREQUEST']._serialized_end=76
  _globals['_GRABRESPONSE']._serialized_start=78
  _globals['_GRABRESPONSE']._serialized_end=151
  _globals['_RELEASEREQUEST']._serialized_start=153
  _globals['_RELEASEREQUEST']._serialized_end=187
  _globals['_RELEASERESPONSE']._serialized_start=189
  _globals['_RELEASERESPONSE']._serialized_end=265
  _globals['_GRIPPERRESULT']._serialized_start=268
  _globals['_GRIPPERRESULT']._serialized_end=514
  _globals['_GRIPPERRESULT_RESULT']._serialized_start=364
  _globals['_GRIPPERRESULT_RESULT']._serialized_end=514
  _globals['_GRIPPERSERVICE']._serialized_start=587
  _globals['_GRIPPERSERVICE']._serialized_end=766
# @@protoc_insertion_point(module_scope)
