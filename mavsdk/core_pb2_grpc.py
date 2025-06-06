# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import core_pb2 as core_dot_core__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in core/core_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class CoreServiceStub(object):
    """Access to the connection state and core configurations
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubscribeConnectionState = channel.unary_stream(
                '/mavsdk.rpc.core.CoreService/SubscribeConnectionState',
                request_serializer=core_dot_core__pb2.SubscribeConnectionStateRequest.SerializeToString,
                response_deserializer=core_dot_core__pb2.ConnectionStateResponse.FromString,
                _registered_method=True)
        self.SetMavlinkTimeout = channel.unary_unary(
                '/mavsdk.rpc.core.CoreService/SetMavlinkTimeout',
                request_serializer=core_dot_core__pb2.SetMavlinkTimeoutRequest.SerializeToString,
                response_deserializer=core_dot_core__pb2.SetMavlinkTimeoutResponse.FromString,
                _registered_method=True)


class CoreServiceServicer(object):
    """Access to the connection state and core configurations
    """

    def SubscribeConnectionState(self, request, context):
        """
        Subscribe to 'connection state' updates.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetMavlinkTimeout(self, request, context):
        """
        Set timeout of MAVLink transfers.

        The default timeout used is generally (0.5 seconds) seconds.
        If MAVSDK is used on the same host this timeout can be reduced, while
        if MAVSDK has to communicate over links with high latency it might
        need to be increased to prevent timeouts.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CoreServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SubscribeConnectionState': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeConnectionState,
                    request_deserializer=core_dot_core__pb2.SubscribeConnectionStateRequest.FromString,
                    response_serializer=core_dot_core__pb2.ConnectionStateResponse.SerializeToString,
            ),
            'SetMavlinkTimeout': grpc.unary_unary_rpc_method_handler(
                    servicer.SetMavlinkTimeout,
                    request_deserializer=core_dot_core__pb2.SetMavlinkTimeoutRequest.FromString,
                    response_serializer=core_dot_core__pb2.SetMavlinkTimeoutResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mavsdk.rpc.core.CoreService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('mavsdk.rpc.core.CoreService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class CoreService(object):
    """Access to the connection state and core configurations
    """

    @staticmethod
    def SubscribeConnectionState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/mavsdk.rpc.core.CoreService/SubscribeConnectionState',
            core_dot_core__pb2.SubscribeConnectionStateRequest.SerializeToString,
            core_dot_core__pb2.ConnectionStateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetMavlinkTimeout(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/mavsdk.rpc.core.CoreService/SetMavlinkTimeout',
            core_dot_core__pb2.SetMavlinkTimeoutRequest.SerializeToString,
            core_dot_core__pb2.SetMavlinkTimeoutResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
