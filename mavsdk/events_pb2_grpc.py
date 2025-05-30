# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import events_pb2 as events_dot_events__pb2

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
        + f' but the generated code in events/events_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class EventsServiceStub(object):
    """Get event notifications, such as takeoff, or arming checks
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubscribeEvents = channel.unary_stream(
                '/mavsdk.rpc.events.EventsService/SubscribeEvents',
                request_serializer=events_dot_events__pb2.SubscribeEventsRequest.SerializeToString,
                response_deserializer=events_dot_events__pb2.EventsResponse.FromString,
                _registered_method=True)
        self.SubscribeHealthAndArmingChecks = channel.unary_stream(
                '/mavsdk.rpc.events.EventsService/SubscribeHealthAndArmingChecks',
                request_serializer=events_dot_events__pb2.SubscribeHealthAndArmingChecksRequest.SerializeToString,
                response_deserializer=events_dot_events__pb2.HealthAndArmingChecksResponse.FromString,
                _registered_method=True)
        self.GetHealthAndArmingChecksReport = channel.unary_unary(
                '/mavsdk.rpc.events.EventsService/GetHealthAndArmingChecksReport',
                request_serializer=events_dot_events__pb2.GetHealthAndArmingChecksReportRequest.SerializeToString,
                response_deserializer=events_dot_events__pb2.GetHealthAndArmingChecksReportResponse.FromString,
                _registered_method=True)


class EventsServiceServicer(object):
    """Get event notifications, such as takeoff, or arming checks
    """

    def SubscribeEvents(self, request, context):
        """
        Subscribe to event updates.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeHealthAndArmingChecks(self, request, context):
        """
        Subscribe to arming check updates.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetHealthAndArmingChecksReport(self, request, context):
        """
        Get the latest report.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EventsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SubscribeEvents': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeEvents,
                    request_deserializer=events_dot_events__pb2.SubscribeEventsRequest.FromString,
                    response_serializer=events_dot_events__pb2.EventsResponse.SerializeToString,
            ),
            'SubscribeHealthAndArmingChecks': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeHealthAndArmingChecks,
                    request_deserializer=events_dot_events__pb2.SubscribeHealthAndArmingChecksRequest.FromString,
                    response_serializer=events_dot_events__pb2.HealthAndArmingChecksResponse.SerializeToString,
            ),
            'GetHealthAndArmingChecksReport': grpc.unary_unary_rpc_method_handler(
                    servicer.GetHealthAndArmingChecksReport,
                    request_deserializer=events_dot_events__pb2.GetHealthAndArmingChecksReportRequest.FromString,
                    response_serializer=events_dot_events__pb2.GetHealthAndArmingChecksReportResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mavsdk.rpc.events.EventsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('mavsdk.rpc.events.EventsService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class EventsService(object):
    """Get event notifications, such as takeoff, or arming checks
    """

    @staticmethod
    def SubscribeEvents(request,
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
            '/mavsdk.rpc.events.EventsService/SubscribeEvents',
            events_dot_events__pb2.SubscribeEventsRequest.SerializeToString,
            events_dot_events__pb2.EventsResponse.FromString,
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
    def SubscribeHealthAndArmingChecks(request,
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
            '/mavsdk.rpc.events.EventsService/SubscribeHealthAndArmingChecks',
            events_dot_events__pb2.SubscribeHealthAndArmingChecksRequest.SerializeToString,
            events_dot_events__pb2.HealthAndArmingChecksResponse.FromString,
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
    def GetHealthAndArmingChecksReport(request,
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
            '/mavsdk.rpc.events.EventsService/GetHealthAndArmingChecksReport',
            events_dot_events__pb2.GetHealthAndArmingChecksReportRequest.SerializeToString,
            events_dot_events__pb2.GetHealthAndArmingChecksReportResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
