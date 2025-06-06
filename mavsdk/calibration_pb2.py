# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: calibration/calibration.proto
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
    'calibration/calibration.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x63\x61libration/calibration.proto\x12\x16mavsdk.rpc.calibration\x1a\x14mavsdk_options.proto\"\x1f\n\x1dSubscribeCalibrateGyroRequest\"\x9b\x01\n\x15\x43\x61librateGyroResponse\x12\x45\n\x12\x63\x61libration_result\x18\x01 \x01(\x0b\x32).mavsdk.rpc.calibration.CalibrationResult\x12;\n\rprogress_data\x18\x02 \x01(\x0b\x32$.mavsdk.rpc.calibration.ProgressData\"(\n&SubscribeCalibrateAccelerometerRequest\"\xa4\x01\n\x1e\x43\x61librateAccelerometerResponse\x12\x45\n\x12\x63\x61libration_result\x18\x01 \x01(\x0b\x32).mavsdk.rpc.calibration.CalibrationResult\x12;\n\rprogress_data\x18\x02 \x01(\x0b\x32$.mavsdk.rpc.calibration.ProgressData\"\'\n%SubscribeCalibrateMagnetometerRequest\"\xa3\x01\n\x1d\x43\x61librateMagnetometerResponse\x12\x45\n\x12\x63\x61libration_result\x18\x01 \x01(\x0b\x32).mavsdk.rpc.calibration.CalibrationResult\x12;\n\rprogress_data\x18\x02 \x01(\x0b\x32$.mavsdk.rpc.calibration.ProgressData\"\'\n%SubscribeCalibrateLevelHorizonRequest\"\xa3\x01\n\x1d\x43\x61librateLevelHorizonResponse\x12\x45\n\x12\x63\x61libration_result\x18\x01 \x01(\x0b\x32).mavsdk.rpc.calibration.CalibrationResult\x12;\n\rprogress_data\x18\x02 \x01(\x0b\x32$.mavsdk.rpc.calibration.ProgressData\".\n,SubscribeCalibrateGimbalAccelerometerRequest\"\xaa\x01\n$CalibrateGimbalAccelerometerResponse\x12\x45\n\x12\x63\x61libration_result\x18\x01 \x01(\x0b\x32).mavsdk.rpc.calibration.CalibrationResult\x12;\n\rprogress_data\x18\x02 \x01(\x0b\x32$.mavsdk.rpc.calibration.ProgressData\"\x0f\n\rCancelRequest\"W\n\x0e\x43\x61ncelResponse\x12\x45\n\x12\x63\x61libration_result\x18\x01 \x01(\x0b\x32).mavsdk.rpc.calibration.CalibrationResult\"\xfa\x02\n\x11\x43\x61librationResult\x12@\n\x06result\x18\x01 \x01(\x0e\x32\x30.mavsdk.rpc.calibration.CalibrationResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\x8e\x02\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x0f\n\x0bRESULT_NEXT\x10\x02\x12\x11\n\rRESULT_FAILED\x10\x03\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x04\x12\x1b\n\x17RESULT_CONNECTION_ERROR\x10\x05\x12\x0f\n\x0bRESULT_BUSY\x10\x06\x12\x19\n\x15RESULT_COMMAND_DENIED\x10\x07\x12\x12\n\x0eRESULT_TIMEOUT\x10\x08\x12\x14\n\x10RESULT_CANCELLED\x10\t\x12\x17\n\x13RESULT_FAILED_ARMED\x10\n\x12\x16\n\x12RESULT_UNSUPPORTED\x10\x0b\"\x83\x01\n\x0cProgressData\x12\x1f\n\x0chas_progress\x18\x01 \x01(\x08\x42\t\x82\xb5\x18\x05\x66\x61lse\x12\x19\n\x08progress\x18\x02 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\"\n\x0fhas_status_text\x18\x03 \x01(\x08\x42\t\x82\xb5\x18\x05\x66\x61lse\x12\x13\n\x0bstatus_text\x18\x04 \x01(\t2\xac\x07\n\x12\x43\x61librationService\x12\x8a\x01\n\x16SubscribeCalibrateGyro\x12\x35.mavsdk.rpc.calibration.SubscribeCalibrateGyroRequest\x1a-.mavsdk.rpc.calibration.CalibrateGyroResponse\"\x08\x80\xb5\x18\x00\x88\xb5\x18\x01\x30\x01\x12\xa5\x01\n\x1fSubscribeCalibrateAccelerometer\x12>.mavsdk.rpc.calibration.SubscribeCalibrateAccelerometerRequest\x1a\x36.mavsdk.rpc.calibration.CalibrateAccelerometerResponse\"\x08\x80\xb5\x18\x00\x88\xb5\x18\x01\x30\x01\x12\xa2\x01\n\x1eSubscribeCalibrateMagnetometer\x12=.mavsdk.rpc.calibration.SubscribeCalibrateMagnetometerRequest\x1a\x35.mavsdk.rpc.calibration.CalibrateMagnetometerResponse\"\x08\x80\xb5\x18\x00\x88\xb5\x18\x01\x30\x01\x12\xa2\x01\n\x1eSubscribeCalibrateLevelHorizon\x12=.mavsdk.rpc.calibration.SubscribeCalibrateLevelHorizonRequest\x1a\x35.mavsdk.rpc.calibration.CalibrateLevelHorizonResponse\"\x08\x80\xb5\x18\x00\x88\xb5\x18\x01\x30\x01\x12\xb7\x01\n%SubscribeCalibrateGimbalAccelerometer\x12\x44.mavsdk.rpc.calibration.SubscribeCalibrateGimbalAccelerometerRequest\x1a<.mavsdk.rpc.calibration.CalibrateGimbalAccelerometerResponse\"\x08\x80\xb5\x18\x00\x88\xb5\x18\x01\x30\x01\x12]\n\x06\x43\x61ncel\x12%.mavsdk.rpc.calibration.CancelRequest\x1a&.mavsdk.rpc.calibration.CancelResponse\"\x04\x80\xb5\x18\x01\x42)\n\x15io.mavsdk.calibrationB\x10\x43\x61librationProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'calibration.calibration_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\025io.mavsdk.calibrationB\020CalibrationProto'
  _globals['_PROGRESSDATA'].fields_by_name['has_progress']._loaded_options = None
  _globals['_PROGRESSDATA'].fields_by_name['has_progress']._serialized_options = b'\202\265\030\005false'
  _globals['_PROGRESSDATA'].fields_by_name['progress']._loaded_options = None
  _globals['_PROGRESSDATA'].fields_by_name['progress']._serialized_options = b'\202\265\030\003NaN'
  _globals['_PROGRESSDATA'].fields_by_name['has_status_text']._loaded_options = None
  _globals['_PROGRESSDATA'].fields_by_name['has_status_text']._serialized_options = b'\202\265\030\005false'
  _globals['_CALIBRATIONSERVICE'].methods_by_name['SubscribeCalibrateGyro']._loaded_options = None
  _globals['_CALIBRATIONSERVICE'].methods_by_name['SubscribeCalibrateGyro']._serialized_options = b'\200\265\030\000\210\265\030\001'
  _globals['_CALIBRATIONSERVICE'].methods_by_name['SubscribeCalibrateAccelerometer']._loaded_options = None
  _globals['_CALIBRATIONSERVICE'].methods_by_name['SubscribeCalibrateAccelerometer']._serialized_options = b'\200\265\030\000\210\265\030\001'
  _globals['_CALIBRATIONSERVICE'].methods_by_name['SubscribeCalibrateMagnetometer']._loaded_options = None
  _globals['_CALIBRATIONSERVICE'].methods_by_name['SubscribeCalibrateMagnetometer']._serialized_options = b'\200\265\030\000\210\265\030\001'
  _globals['_CALIBRATIONSERVICE'].methods_by_name['SubscribeCalibrateLevelHorizon']._loaded_options = None
  _globals['_CALIBRATIONSERVICE'].methods_by_name['SubscribeCalibrateLevelHorizon']._serialized_options = b'\200\265\030\000\210\265\030\001'
  _globals['_CALIBRATIONSERVICE'].methods_by_name['SubscribeCalibrateGimbalAccelerometer']._loaded_options = None
  _globals['_CALIBRATIONSERVICE'].methods_by_name['SubscribeCalibrateGimbalAccelerometer']._serialized_options = b'\200\265\030\000\210\265\030\001'
  _globals['_CALIBRATIONSERVICE'].methods_by_name['Cancel']._loaded_options = None
  _globals['_CALIBRATIONSERVICE'].methods_by_name['Cancel']._serialized_options = b'\200\265\030\001'
  _globals['_SUBSCRIBECALIBRATEGYROREQUEST']._serialized_start=79
  _globals['_SUBSCRIBECALIBRATEGYROREQUEST']._serialized_end=110
  _globals['_CALIBRATEGYRORESPONSE']._serialized_start=113
  _globals['_CALIBRATEGYRORESPONSE']._serialized_end=268
  _globals['_SUBSCRIBECALIBRATEACCELEROMETERREQUEST']._serialized_start=270
  _globals['_SUBSCRIBECALIBRATEACCELEROMETERREQUEST']._serialized_end=310
  _globals['_CALIBRATEACCELEROMETERRESPONSE']._serialized_start=313
  _globals['_CALIBRATEACCELEROMETERRESPONSE']._serialized_end=477
  _globals['_SUBSCRIBECALIBRATEMAGNETOMETERREQUEST']._serialized_start=479
  _globals['_SUBSCRIBECALIBRATEMAGNETOMETERREQUEST']._serialized_end=518
  _globals['_CALIBRATEMAGNETOMETERRESPONSE']._serialized_start=521
  _globals['_CALIBRATEMAGNETOMETERRESPONSE']._serialized_end=684
  _globals['_SUBSCRIBECALIBRATELEVELHORIZONREQUEST']._serialized_start=686
  _globals['_SUBSCRIBECALIBRATELEVELHORIZONREQUEST']._serialized_end=725
  _globals['_CALIBRATELEVELHORIZONRESPONSE']._serialized_start=728
  _globals['_CALIBRATELEVELHORIZONRESPONSE']._serialized_end=891
  _globals['_SUBSCRIBECALIBRATEGIMBALACCELEROMETERREQUEST']._serialized_start=893
  _globals['_SUBSCRIBECALIBRATEGIMBALACCELEROMETERREQUEST']._serialized_end=939
  _globals['_CALIBRATEGIMBALACCELEROMETERRESPONSE']._serialized_start=942
  _globals['_CALIBRATEGIMBALACCELEROMETERRESPONSE']._serialized_end=1112
  _globals['_CANCELREQUEST']._serialized_start=1114
  _globals['_CANCELREQUEST']._serialized_end=1129
  _globals['_CANCELRESPONSE']._serialized_start=1131
  _globals['_CANCELRESPONSE']._serialized_end=1218
  _globals['_CALIBRATIONRESULT']._serialized_start=1221
  _globals['_CALIBRATIONRESULT']._serialized_end=1599
  _globals['_CALIBRATIONRESULT_RESULT']._serialized_start=1329
  _globals['_CALIBRATIONRESULT_RESULT']._serialized_end=1599
  _globals['_PROGRESSDATA']._serialized_start=1602
  _globals['_PROGRESSDATA']._serialized_end=1733
  _globals['_CALIBRATIONSERVICE']._serialized_start=1736
  _globals['_CALIBRATIONSERVICE']._serialized_end=2676
# @@protoc_insertion_point(module_scope)
