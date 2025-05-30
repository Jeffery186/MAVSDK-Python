# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: events/events.proto
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
    'events/events.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x65vents/events.proto\x12\x11mavsdk.rpc.events\x1a\x14mavsdk_options.proto\"\x9a\x01\n\x05\x45vent\x12\x0e\n\x06\x63ompid\x18\x01 \x01(\r\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12.\n\tlog_level\x18\x04 \x01(\x0e\x32\x1b.mavsdk.rpc.events.LogLevel\x12\x17\n\x0f\x65vent_namespace\x18\x05 \x01(\t\x12\x12\n\nevent_name\x18\x06 \x01(\t\"\x8d\x01\n\x1bHealthAndArmingCheckProblem\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12.\n\tlog_level\x18\x03 \x01(\x0e\x32\x1b.mavsdk.rpc.events.LogLevel\x12\x18\n\x10health_component\x18\x04 \x01(\t\"\x87\x01\n\x18HealthAndArmingCheckMode\x12\x11\n\tmode_name\x18\x01 \x01(\t\x12\x16\n\x0e\x63\x61n_arm_or_run\x18\x02 \x01(\x08\x12@\n\x08problems\x18\x03 \x03(\x0b\x32..mavsdk.rpc.events.HealthAndArmingCheckProblem\"p\n\x15HealthComponentReport\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05label\x18\x02 \x01(\t\x12\x12\n\nis_present\x18\x03 \x01(\x08\x12\x11\n\thas_error\x18\x04 \x01(\x08\x12\x13\n\x0bhas_warning\x18\x05 \x01(\x08\"\xf4\x01\n\x1aHealthAndArmingCheckReport\x12K\n\x16\x63urrent_mode_intention\x18\x01 \x01(\x0b\x32+.mavsdk.rpc.events.HealthAndArmingCheckMode\x12\x43\n\x11health_components\x18\x02 \x03(\x0b\x32(.mavsdk.rpc.events.HealthComponentReport\x12\x44\n\x0c\x61ll_problems\x18\x03 \x03(\x0b\x32..mavsdk.rpc.events.HealthAndArmingCheckProblem\"\xac\x02\n\x0c\x45ventsResult\x12\x36\n\x06result\x18\x01 \x01(\x0e\x32&.mavsdk.rpc.events.EventsResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\xcf\x01\n\x06Result\x12\x12\n\x0eRESULT_SUCCESS\x10\x00\x12\x18\n\x14RESULT_NOT_AVAILABLE\x10\x01\x12\x1b\n\x17RESULT_CONNECTION_ERROR\x10\x02\x12\x16\n\x12RESULT_UNSUPPORTED\x10\x03\x12\x11\n\rRESULT_DENIED\x10\x04\x12\x11\n\rRESULT_FAILED\x10\x05\x12\x12\n\x0eRESULT_TIMEOUT\x10\x06\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x07\x12\x12\n\x0eRESULT_UNKNOWN\x10\x08\"\x18\n\x16SubscribeEventsRequest\"9\n\x0e\x45ventsResponse\x12\'\n\x05\x65vent\x18\x01 \x01(\x0b\x32\x18.mavsdk.rpc.events.Event\"\'\n%SubscribeHealthAndArmingChecksRequest\"^\n\x1dHealthAndArmingChecksResponse\x12=\n\x06report\x18\x01 \x01(\x0b\x32-.mavsdk.rpc.events.HealthAndArmingCheckReport\"\'\n%GetHealthAndArmingChecksReportRequest\"\x9f\x01\n&GetHealthAndArmingChecksReportResponse\x12\x36\n\revents_result\x18\x01 \x01(\x0b\x32\x1f.mavsdk.rpc.events.EventsResult\x12=\n\x06report\x18\x02 \x01(\x0b\x32-.mavsdk.rpc.events.HealthAndArmingCheckReport*\xbb\x01\n\x08LogLevel\x12\x17\n\x13LOG_LEVEL_EMERGENCY\x10\x00\x12\x13\n\x0fLOG_LEVEL_ALERT\x10\x01\x12\x16\n\x12LOG_LEVEL_CRITICAL\x10\x02\x12\x13\n\x0fLOG_LEVEL_ERROR\x10\x03\x12\x15\n\x11LOG_LEVEL_WARNING\x10\x04\x12\x14\n\x10LOG_LEVEL_NOTICE\x10\x05\x12\x12\n\x0eLOG_LEVEL_INFO\x10\x06\x12\x13\n\x0fLOG_LEVEL_DEBUG\x10\x07\x32\xad\x03\n\rEventsService\x12g\n\x0fSubscribeEvents\x12).mavsdk.rpc.events.SubscribeEventsRequest\x1a!.mavsdk.rpc.events.EventsResponse\"\x04\x80\xb5\x18\x00\x30\x01\x12\x94\x01\n\x1eSubscribeHealthAndArmingChecks\x12\x38.mavsdk.rpc.events.SubscribeHealthAndArmingChecksRequest\x1a\x30.mavsdk.rpc.events.HealthAndArmingChecksResponse\"\x04\x80\xb5\x18\x00\x30\x01\x12\x9b\x01\n\x1eGetHealthAndArmingChecksReport\x12\x38.mavsdk.rpc.events.GetHealthAndArmingChecksReportRequest\x1a\x39.mavsdk.rpc.events.GetHealthAndArmingChecksReportResponse\"\x04\x80\xb5\x18\x01\x42\x1f\n\x10io.mavsdk.eventsB\x0b\x45ventsProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'events.events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\020io.mavsdk.eventsB\013EventsProto'
  _globals['_EVENTSSERVICE'].methods_by_name['SubscribeEvents']._loaded_options = None
  _globals['_EVENTSSERVICE'].methods_by_name['SubscribeEvents']._serialized_options = b'\200\265\030\000'
  _globals['_EVENTSSERVICE'].methods_by_name['SubscribeHealthAndArmingChecks']._loaded_options = None
  _globals['_EVENTSSERVICE'].methods_by_name['SubscribeHealthAndArmingChecks']._serialized_options = b'\200\265\030\000'
  _globals['_EVENTSSERVICE'].methods_by_name['GetHealthAndArmingChecksReport']._loaded_options = None
  _globals['_EVENTSSERVICE'].methods_by_name['GetHealthAndArmingChecksReport']._serialized_options = b'\200\265\030\001'
  _globals['_LOGLEVEL']._serialized_start=1593
  _globals['_LOGLEVEL']._serialized_end=1780
  _globals['_EVENT']._serialized_start=65
  _globals['_EVENT']._serialized_end=219
  _globals['_HEALTHANDARMINGCHECKPROBLEM']._serialized_start=222
  _globals['_HEALTHANDARMINGCHECKPROBLEM']._serialized_end=363
  _globals['_HEALTHANDARMINGCHECKMODE']._serialized_start=366
  _globals['_HEALTHANDARMINGCHECKMODE']._serialized_end=501
  _globals['_HEALTHCOMPONENTREPORT']._serialized_start=503
  _globals['_HEALTHCOMPONENTREPORT']._serialized_end=615
  _globals['_HEALTHANDARMINGCHECKREPORT']._serialized_start=618
  _globals['_HEALTHANDARMINGCHECKREPORT']._serialized_end=862
  _globals['_EVENTSRESULT']._serialized_start=865
  _globals['_EVENTSRESULT']._serialized_end=1165
  _globals['_EVENTSRESULT_RESULT']._serialized_start=958
  _globals['_EVENTSRESULT_RESULT']._serialized_end=1165
  _globals['_SUBSCRIBEEVENTSREQUEST']._serialized_start=1167
  _globals['_SUBSCRIBEEVENTSREQUEST']._serialized_end=1191
  _globals['_EVENTSRESPONSE']._serialized_start=1193
  _globals['_EVENTSRESPONSE']._serialized_end=1250
  _globals['_SUBSCRIBEHEALTHANDARMINGCHECKSREQUEST']._serialized_start=1252
  _globals['_SUBSCRIBEHEALTHANDARMINGCHECKSREQUEST']._serialized_end=1291
  _globals['_HEALTHANDARMINGCHECKSRESPONSE']._serialized_start=1293
  _globals['_HEALTHANDARMINGCHECKSRESPONSE']._serialized_end=1387
  _globals['_GETHEALTHANDARMINGCHECKSREPORTREQUEST']._serialized_start=1389
  _globals['_GETHEALTHANDARMINGCHECKSREPORTREQUEST']._serialized_end=1428
  _globals['_GETHEALTHANDARMINGCHECKSREPORTRESPONSE']._serialized_start=1431
  _globals['_GETHEALTHANDARMINGCHECKSREPORTRESPONSE']._serialized_end=1590
  _globals['_EVENTSSERVICE']._serialized_start=1783
  _globals['_EVENTSSERVICE']._serialized_end=2212
# @@protoc_insertion_point(module_scope)
