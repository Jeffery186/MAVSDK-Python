# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import mission_pb2 as mission_dot_mission__pb2

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
        + f' but the generated code in mission/mission_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class MissionServiceStub(object):
    """Enable waypoint missions.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UploadMission = channel.unary_unary(
                '/mavsdk.rpc.mission.MissionService/UploadMission',
                request_serializer=mission_dot_mission__pb2.UploadMissionRequest.SerializeToString,
                response_deserializer=mission_dot_mission__pb2.UploadMissionResponse.FromString,
                _registered_method=True)
        self.SubscribeUploadMissionWithProgress = channel.unary_stream(
                '/mavsdk.rpc.mission.MissionService/SubscribeUploadMissionWithProgress',
                request_serializer=mission_dot_mission__pb2.SubscribeUploadMissionWithProgressRequest.SerializeToString,
                response_deserializer=mission_dot_mission__pb2.UploadMissionWithProgressResponse.FromString,
                _registered_method=True)
        self.CancelMissionUpload = channel.unary_unary(
                '/mavsdk.rpc.mission.MissionService/CancelMissionUpload',
                request_serializer=mission_dot_mission__pb2.CancelMissionUploadRequest.SerializeToString,
                response_deserializer=mission_dot_mission__pb2.CancelMissionUploadResponse.FromString,
                _registered_method=True)
        self.DownloadMission = channel.unary_unary(
                '/mavsdk.rpc.mission.MissionService/DownloadMission',
                request_serializer=mission_dot_mission__pb2.DownloadMissionRequest.SerializeToString,
                response_deserializer=mission_dot_mission__pb2.DownloadMissionResponse.FromString,
                _registered_method=True)
        self.SubscribeDownloadMissionWithProgress = channel.unary_stream(
                '/mavsdk.rpc.mission.MissionService/SubscribeDownloadMissionWithProgress',
                request_serializer=mission_dot_mission__pb2.SubscribeDownloadMissionWithProgressRequest.SerializeToString,
                response_deserializer=mission_dot_mission__pb2.DownloadMissionWithProgressResponse.FromString,
                _registered_method=True)
        self.CancelMissionDownload = channel.unary_unary(
                '/mavsdk.rpc.mission.MissionService/CancelMissionDownload',
                request_serializer=mission_dot_mission__pb2.CancelMissionDownloadRequest.SerializeToString,
                response_deserializer=mission_dot_mission__pb2.CancelMissionDownloadResponse.FromString,
                _registered_method=True)
        self.StartMission = channel.unary_unary(
                '/mavsdk.rpc.mission.MissionService/StartMission',
                request_serializer=mission_dot_mission__pb2.StartMissionRequest.SerializeToString,
                response_deserializer=mission_dot_mission__pb2.StartMissionResponse.FromString,
                _registered_method=True)
        self.PauseMission = channel.unary_unary(
                '/mavsdk.rpc.mission.MissionService/PauseMission',
                request_serializer=mission_dot_mission__pb2.PauseMissionRequest.SerializeToString,
                response_deserializer=mission_dot_mission__pb2.PauseMissionResponse.FromString,
                _registered_method=True)
        self.ClearMission = channel.unary_unary(
                '/mavsdk.rpc.mission.MissionService/ClearMission',
                request_serializer=mission_dot_mission__pb2.ClearMissionRequest.SerializeToString,
                response_deserializer=mission_dot_mission__pb2.ClearMissionResponse.FromString,
                _registered_method=True)
        self.SetCurrentMissionItem = channel.unary_unary(
                '/mavsdk.rpc.mission.MissionService/SetCurrentMissionItem',
                request_serializer=mission_dot_mission__pb2.SetCurrentMissionItemRequest.SerializeToString,
                response_deserializer=mission_dot_mission__pb2.SetCurrentMissionItemResponse.FromString,
                _registered_method=True)
        self.IsMissionFinished = channel.unary_unary(
                '/mavsdk.rpc.mission.MissionService/IsMissionFinished',
                request_serializer=mission_dot_mission__pb2.IsMissionFinishedRequest.SerializeToString,
                response_deserializer=mission_dot_mission__pb2.IsMissionFinishedResponse.FromString,
                _registered_method=True)
        self.SubscribeMissionProgress = channel.unary_stream(
                '/mavsdk.rpc.mission.MissionService/SubscribeMissionProgress',
                request_serializer=mission_dot_mission__pb2.SubscribeMissionProgressRequest.SerializeToString,
                response_deserializer=mission_dot_mission__pb2.MissionProgressResponse.FromString,
                _registered_method=True)
        self.GetReturnToLaunchAfterMission = channel.unary_unary(
                '/mavsdk.rpc.mission.MissionService/GetReturnToLaunchAfterMission',
                request_serializer=mission_dot_mission__pb2.GetReturnToLaunchAfterMissionRequest.SerializeToString,
                response_deserializer=mission_dot_mission__pb2.GetReturnToLaunchAfterMissionResponse.FromString,
                _registered_method=True)
        self.SetReturnToLaunchAfterMission = channel.unary_unary(
                '/mavsdk.rpc.mission.MissionService/SetReturnToLaunchAfterMission',
                request_serializer=mission_dot_mission__pb2.SetReturnToLaunchAfterMissionRequest.SerializeToString,
                response_deserializer=mission_dot_mission__pb2.SetReturnToLaunchAfterMissionResponse.FromString,
                _registered_method=True)


class MissionServiceServicer(object):
    """Enable waypoint missions.
    """

    def UploadMission(self, request, context):
        """
        Upload a list of mission items to the system.

        The mission items are uploaded to a drone. Once uploaded the mission can be started and
        executed even if the connection is lost.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeUploadMissionWithProgress(self, request, context):
        """
        Upload a list of mission items to the system and report upload progress.

        The mission items are uploaded to a drone. Once uploaded the mission can be started and
        executed even if the connection is lost.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelMissionUpload(self, request, context):
        """
        Cancel an ongoing mission upload.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DownloadMission(self, request, context):
        """
        Download a list of mission items from the system (asynchronous).

        Will fail if any of the downloaded mission items are not supported
        by the MAVSDK API.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeDownloadMissionWithProgress(self, request, context):
        """
        Download a list of mission items from the system (asynchronous) and report progress.

        Will fail if any of the downloaded mission items are not supported
        by the MAVSDK API.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelMissionDownload(self, request, context):
        """
        Cancel an ongoing mission download.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartMission(self, request, context):
        """
        Start the mission.

        A mission must be uploaded to the vehicle before this can be called.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PauseMission(self, request, context):
        """
        Pause the mission.

        Pausing the mission puts the vehicle into
        [HOLD mode](https://docs.px4.io/en/flight_modes/hold.html).
        A multicopter should just hover at the spot while a fixedwing vehicle should loiter
        around the location where it paused.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClearMission(self, request, context):
        """
        Clear the mission saved on the vehicle.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetCurrentMissionItem(self, request, context):
        """
        Sets the mission item index to go to.

        By setting the current index to 0, the mission is restarted from the beginning. If it is set
        to a specific index of a mission item, the mission will be set to this item.

        Note that this is not necessarily true for general missions using MAVLink if loop counters
        are used.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IsMissionFinished(self, request, context):
        """
        Check if the mission has been finished.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeMissionProgress(self, request, context):
        """
        Subscribe to mission progress updates.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetReturnToLaunchAfterMission(self, request, context):
        """
        Get whether to trigger Return-to-Launch (RTL) after mission is complete.

        Before getting this option, it needs to be set, or a mission
        needs to be downloaded.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetReturnToLaunchAfterMission(self, request, context):
        """
        Set whether to trigger Return-to-Launch (RTL) after the mission is complete.

        This will only take effect for the next mission upload, meaning that
        the mission may have to be uploaded again.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MissionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UploadMission': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadMission,
                    request_deserializer=mission_dot_mission__pb2.UploadMissionRequest.FromString,
                    response_serializer=mission_dot_mission__pb2.UploadMissionResponse.SerializeToString,
            ),
            'SubscribeUploadMissionWithProgress': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeUploadMissionWithProgress,
                    request_deserializer=mission_dot_mission__pb2.SubscribeUploadMissionWithProgressRequest.FromString,
                    response_serializer=mission_dot_mission__pb2.UploadMissionWithProgressResponse.SerializeToString,
            ),
            'CancelMissionUpload': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelMissionUpload,
                    request_deserializer=mission_dot_mission__pb2.CancelMissionUploadRequest.FromString,
                    response_serializer=mission_dot_mission__pb2.CancelMissionUploadResponse.SerializeToString,
            ),
            'DownloadMission': grpc.unary_unary_rpc_method_handler(
                    servicer.DownloadMission,
                    request_deserializer=mission_dot_mission__pb2.DownloadMissionRequest.FromString,
                    response_serializer=mission_dot_mission__pb2.DownloadMissionResponse.SerializeToString,
            ),
            'SubscribeDownloadMissionWithProgress': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeDownloadMissionWithProgress,
                    request_deserializer=mission_dot_mission__pb2.SubscribeDownloadMissionWithProgressRequest.FromString,
                    response_serializer=mission_dot_mission__pb2.DownloadMissionWithProgressResponse.SerializeToString,
            ),
            'CancelMissionDownload': grpc.unary_unary_rpc_method_handler(
                    servicer.CancelMissionDownload,
                    request_deserializer=mission_dot_mission__pb2.CancelMissionDownloadRequest.FromString,
                    response_serializer=mission_dot_mission__pb2.CancelMissionDownloadResponse.SerializeToString,
            ),
            'StartMission': grpc.unary_unary_rpc_method_handler(
                    servicer.StartMission,
                    request_deserializer=mission_dot_mission__pb2.StartMissionRequest.FromString,
                    response_serializer=mission_dot_mission__pb2.StartMissionResponse.SerializeToString,
            ),
            'PauseMission': grpc.unary_unary_rpc_method_handler(
                    servicer.PauseMission,
                    request_deserializer=mission_dot_mission__pb2.PauseMissionRequest.FromString,
                    response_serializer=mission_dot_mission__pb2.PauseMissionResponse.SerializeToString,
            ),
            'ClearMission': grpc.unary_unary_rpc_method_handler(
                    servicer.ClearMission,
                    request_deserializer=mission_dot_mission__pb2.ClearMissionRequest.FromString,
                    response_serializer=mission_dot_mission__pb2.ClearMissionResponse.SerializeToString,
            ),
            'SetCurrentMissionItem': grpc.unary_unary_rpc_method_handler(
                    servicer.SetCurrentMissionItem,
                    request_deserializer=mission_dot_mission__pb2.SetCurrentMissionItemRequest.FromString,
                    response_serializer=mission_dot_mission__pb2.SetCurrentMissionItemResponse.SerializeToString,
            ),
            'IsMissionFinished': grpc.unary_unary_rpc_method_handler(
                    servicer.IsMissionFinished,
                    request_deserializer=mission_dot_mission__pb2.IsMissionFinishedRequest.FromString,
                    response_serializer=mission_dot_mission__pb2.IsMissionFinishedResponse.SerializeToString,
            ),
            'SubscribeMissionProgress': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeMissionProgress,
                    request_deserializer=mission_dot_mission__pb2.SubscribeMissionProgressRequest.FromString,
                    response_serializer=mission_dot_mission__pb2.MissionProgressResponse.SerializeToString,
            ),
            'GetReturnToLaunchAfterMission': grpc.unary_unary_rpc_method_handler(
                    servicer.GetReturnToLaunchAfterMission,
                    request_deserializer=mission_dot_mission__pb2.GetReturnToLaunchAfterMissionRequest.FromString,
                    response_serializer=mission_dot_mission__pb2.GetReturnToLaunchAfterMissionResponse.SerializeToString,
            ),
            'SetReturnToLaunchAfterMission': grpc.unary_unary_rpc_method_handler(
                    servicer.SetReturnToLaunchAfterMission,
                    request_deserializer=mission_dot_mission__pb2.SetReturnToLaunchAfterMissionRequest.FromString,
                    response_serializer=mission_dot_mission__pb2.SetReturnToLaunchAfterMissionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mavsdk.rpc.mission.MissionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('mavsdk.rpc.mission.MissionService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class MissionService(object):
    """Enable waypoint missions.
    """

    @staticmethod
    def UploadMission(request,
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
            '/mavsdk.rpc.mission.MissionService/UploadMission',
            mission_dot_mission__pb2.UploadMissionRequest.SerializeToString,
            mission_dot_mission__pb2.UploadMissionResponse.FromString,
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
    def SubscribeUploadMissionWithProgress(request,
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
            '/mavsdk.rpc.mission.MissionService/SubscribeUploadMissionWithProgress',
            mission_dot_mission__pb2.SubscribeUploadMissionWithProgressRequest.SerializeToString,
            mission_dot_mission__pb2.UploadMissionWithProgressResponse.FromString,
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
    def CancelMissionUpload(request,
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
            '/mavsdk.rpc.mission.MissionService/CancelMissionUpload',
            mission_dot_mission__pb2.CancelMissionUploadRequest.SerializeToString,
            mission_dot_mission__pb2.CancelMissionUploadResponse.FromString,
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
    def DownloadMission(request,
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
            '/mavsdk.rpc.mission.MissionService/DownloadMission',
            mission_dot_mission__pb2.DownloadMissionRequest.SerializeToString,
            mission_dot_mission__pb2.DownloadMissionResponse.FromString,
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
    def SubscribeDownloadMissionWithProgress(request,
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
            '/mavsdk.rpc.mission.MissionService/SubscribeDownloadMissionWithProgress',
            mission_dot_mission__pb2.SubscribeDownloadMissionWithProgressRequest.SerializeToString,
            mission_dot_mission__pb2.DownloadMissionWithProgressResponse.FromString,
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
    def CancelMissionDownload(request,
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
            '/mavsdk.rpc.mission.MissionService/CancelMissionDownload',
            mission_dot_mission__pb2.CancelMissionDownloadRequest.SerializeToString,
            mission_dot_mission__pb2.CancelMissionDownloadResponse.FromString,
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
    def StartMission(request,
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
            '/mavsdk.rpc.mission.MissionService/StartMission',
            mission_dot_mission__pb2.StartMissionRequest.SerializeToString,
            mission_dot_mission__pb2.StartMissionResponse.FromString,
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
    def PauseMission(request,
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
            '/mavsdk.rpc.mission.MissionService/PauseMission',
            mission_dot_mission__pb2.PauseMissionRequest.SerializeToString,
            mission_dot_mission__pb2.PauseMissionResponse.FromString,
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
    def ClearMission(request,
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
            '/mavsdk.rpc.mission.MissionService/ClearMission',
            mission_dot_mission__pb2.ClearMissionRequest.SerializeToString,
            mission_dot_mission__pb2.ClearMissionResponse.FromString,
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
    def SetCurrentMissionItem(request,
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
            '/mavsdk.rpc.mission.MissionService/SetCurrentMissionItem',
            mission_dot_mission__pb2.SetCurrentMissionItemRequest.SerializeToString,
            mission_dot_mission__pb2.SetCurrentMissionItemResponse.FromString,
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
    def IsMissionFinished(request,
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
            '/mavsdk.rpc.mission.MissionService/IsMissionFinished',
            mission_dot_mission__pb2.IsMissionFinishedRequest.SerializeToString,
            mission_dot_mission__pb2.IsMissionFinishedResponse.FromString,
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
    def SubscribeMissionProgress(request,
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
            '/mavsdk.rpc.mission.MissionService/SubscribeMissionProgress',
            mission_dot_mission__pb2.SubscribeMissionProgressRequest.SerializeToString,
            mission_dot_mission__pb2.MissionProgressResponse.FromString,
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
    def GetReturnToLaunchAfterMission(request,
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
            '/mavsdk.rpc.mission.MissionService/GetReturnToLaunchAfterMission',
            mission_dot_mission__pb2.GetReturnToLaunchAfterMissionRequest.SerializeToString,
            mission_dot_mission__pb2.GetReturnToLaunchAfterMissionResponse.FromString,
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
    def SetReturnToLaunchAfterMission(request,
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
            '/mavsdk.rpc.mission.MissionService/SetReturnToLaunchAfterMission',
            mission_dot_mission__pb2.SetReturnToLaunchAfterMissionRequest.SerializeToString,
            mission_dot_mission__pb2.SetReturnToLaunchAfterMissionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
