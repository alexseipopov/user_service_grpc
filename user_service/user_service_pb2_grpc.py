# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import user_service.user_service_pb2 as user__service__pb2


class UserServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.get_rp = channel.unary_unary(
                '/user_service.UserService/get_rp',
                request_serializer=user__service__pb2.GetRpRequest.SerializeToString,
                response_deserializer=user__service__pb2.GetRpResponse.FromString,
                )
        self.set_avatar = channel.unary_unary(
                '/user_service.UserService/set_avatar',
                request_serializer=user__service__pb2.SetAvatarRequest.SerializeToString,
                response_deserializer=user__service__pb2.SetAvatarResponse.FromString,
                )
        self.get_avatar = channel.unary_unary(
                '/user_service.UserService/get_avatar',
                request_serializer=user__service__pb2.GetAvatarRequest.SerializeToString,
                response_deserializer=user__service__pb2.GetAvatarResponse.FromString,
                )
        self.get_peer_info = channel.unary_unary(
                '/user_service.UserService/get_peer_info',
                request_serializer=user__service__pb2.GetPeerInfoRequest.SerializeToString,
                response_deserializer=user__service__pb2.GetPeerInfoResponse.FromString,
                )


class UserServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def get_rp(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def set_avatar(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_avatar(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_peer_info(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'get_rp': grpc.unary_unary_rpc_method_handler(
                    servicer.get_rp,
                    request_deserializer=user__service__pb2.GetRpRequest.FromString,
                    response_serializer=user__service__pb2.GetRpResponse.SerializeToString,
            ),
            'set_avatar': grpc.unary_unary_rpc_method_handler(
                    servicer.set_avatar,
                    request_deserializer=user__service__pb2.SetAvatarRequest.FromString,
                    response_serializer=user__service__pb2.SetAvatarResponse.SerializeToString,
            ),
            'get_avatar': grpc.unary_unary_rpc_method_handler(
                    servicer.get_avatar,
                    request_deserializer=user__service__pb2.GetAvatarRequest.FromString,
                    response_serializer=user__service__pb2.GetAvatarResponse.SerializeToString,
            ),
            'get_peer_info': grpc.unary_unary_rpc_method_handler(
                    servicer.get_peer_info,
                    request_deserializer=user__service__pb2.GetPeerInfoRequest.FromString,
                    response_serializer=user__service__pb2.GetPeerInfoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'user_service.UserService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def get_rp(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user_service.UserService/get_rp',
            user__service__pb2.GetRpRequest.SerializeToString,
            user__service__pb2.GetRpResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def set_avatar(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user_service.UserService/set_avatar',
            user__service__pb2.SetAvatarRequest.SerializeToString,
            user__service__pb2.SetAvatarResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_avatar(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user_service.UserService/get_avatar',
            user__service__pb2.GetAvatarRequest.SerializeToString,
            user__service__pb2.GetAvatarResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_peer_info(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/user_service.UserService/get_peer_info',
            user__service__pb2.GetPeerInfoRequest.SerializeToString,
            user__service__pb2.GetPeerInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
