# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import mafia_pb2 as mafia__pb2


class MafiaStub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.add_user = channel.unary_unary(
            '/mafiaservice.Mafia/add_user',
            request_serializer=mafia__pb2.AddUserRequest.SerializeToString,
            response_deserializer=mafia__pb2.Response.FromString,
        )
        self.delete_user = channel.unary_unary(
            '/mafiaservice.Mafia/delete_user',
            request_serializer=mafia__pb2.BaseUserRequest.SerializeToString,
            response_deserializer=mafia__pb2.Response.FromString,
        )
        self.get_users = channel.unary_unary(
            '/mafiaservice.Mafia/get_users',
            request_serializer=mafia__pb2.Empty.SerializeToString,
            response_deserializer=mafia__pb2.Response.FromString,
        )
        self.accuse_user = channel.unary_unary(
            '/mafiaservice.Mafia/accuse_user',
            request_serializer=mafia__pb2.AccuseUserRequest.SerializeToString,
            response_deserializer=mafia__pb2.Response.FromString,
        )
        self.vote_finish_day = channel.unary_unary(
            '/mafiaservice.Mafia/vote_finish_day',
            request_serializer=mafia__pb2.BaseUserRequest.SerializeToString,
            response_deserializer=mafia__pb2.Response.FromString,
        )
        self.init_communication_channel = channel.stream_stream(
            '/mafiaservice.Mafia/init_communication_channel',
            request_serializer=mafia__pb2.CommunicationRequest.SerializeToString,
            response_deserializer=mafia__pb2.CommunicationResponse.FromString,
        )


class MafiaServicer(object):
    """The greeting service definition.
    """

    def add_user(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete_user(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_users(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def accuse_user(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def vote_finish_day(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def init_communication_channel(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MafiaServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'add_user':
            grpc.unary_unary_rpc_method_handler(
                servicer.add_user,
                request_deserializer=mafia__pb2.AddUserRequest.FromString,
                response_serializer=mafia__pb2.Response.SerializeToString,
            ),
        'delete_user':
            grpc.unary_unary_rpc_method_handler(
                servicer.delete_user,
                request_deserializer=mafia__pb2.BaseUserRequest.FromString,
                response_serializer=mafia__pb2.Response.SerializeToString,
            ),
        'get_users':
            grpc.unary_unary_rpc_method_handler(
                servicer.get_users,
                request_deserializer=mafia__pb2.Empty.FromString,
                response_serializer=mafia__pb2.Response.SerializeToString,
            ),
        'accuse_user':
            grpc.unary_unary_rpc_method_handler(
                servicer.accuse_user,
                request_deserializer=mafia__pb2.AccuseUserRequest.FromString,
                response_serializer=mafia__pb2.Response.SerializeToString,
            ),
        'vote_finish_day':
            grpc.unary_unary_rpc_method_handler(
                servicer.vote_finish_day,
                request_deserializer=mafia__pb2.BaseUserRequest.FromString,
                response_serializer=mafia__pb2.Response.SerializeToString,
            ),
        'init_communication_channel':
            grpc.stream_stream_rpc_method_handler(
                servicer.init_communication_channel,
                request_deserializer=mafia__pb2.CommunicationRequest.FromString,
                response_serializer=mafia__pb2.CommunicationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler('mafiaservice.Mafia', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler, ))


# This class is part of an EXPERIMENTAL API.
class Mafia(object):
    """The greeting service definition.
    """

    @staticmethod
    def add_user(request,
                 target,
                 options=(),
                 channel_credentials=None,
                 call_credentials=None,
                 insecure=False,
                 compression=None,
                 wait_for_ready=None,
                 timeout=None,
                 metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafiaservice.Mafia/add_user',
                                             mafia__pb2.AddUserRequest.SerializeToString,
                                             mafia__pb2.Response.FromString, options, channel_credentials, insecure,
                                             call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete_user(request,
                    target,
                    options=(),
                    channel_credentials=None,
                    call_credentials=None,
                    insecure=False,
                    compression=None,
                    wait_for_ready=None,
                    timeout=None,
                    metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafiaservice.Mafia/delete_user',
                                             mafia__pb2.BaseUserRequest.SerializeToString,
                                             mafia__pb2.Response.FromString, options, channel_credentials, insecure,
                                             call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_users(request,
                  target,
                  options=(),
                  channel_credentials=None,
                  call_credentials=None,
                  insecure=False,
                  compression=None,
                  wait_for_ready=None,
                  timeout=None,
                  metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafiaservice.Mafia/get_users',
                                             mafia__pb2.Empty.SerializeToString, mafia__pb2.Response.FromString,
                                             options, channel_credentials, insecure, call_credentials, compression,
                                             wait_for_ready, timeout, metadata)

    @staticmethod
    def accuse_user(request,
                    target,
                    options=(),
                    channel_credentials=None,
                    call_credentials=None,
                    insecure=False,
                    compression=None,
                    wait_for_ready=None,
                    timeout=None,
                    metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafiaservice.Mafia/accuse_user',
                                             mafia__pb2.AccuseUserRequest.SerializeToString,
                                             mafia__pb2.Response.FromString, options, channel_credentials, insecure,
                                             call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def vote_finish_day(request,
                        target,
                        options=(),
                        channel_credentials=None,
                        call_credentials=None,
                        insecure=False,
                        compression=None,
                        wait_for_ready=None,
                        timeout=None,
                        metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mafiaservice.Mafia/vote_finish_day',
                                             mafia__pb2.BaseUserRequest.SerializeToString,
                                             mafia__pb2.Response.FromString, options, channel_credentials, insecure,
                                             call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def init_communication_channel(request_iterator,
                                   target,
                                   options=(),
                                   channel_credentials=None,
                                   call_credentials=None,
                                   insecure=False,
                                   compression=None,
                                   wait_for_ready=None,
                                   timeout=None,
                                   metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator, target, '/mafiaservice.Mafia/init_communication_channel',
            mafia__pb2.CommunicationRequest.SerializeToString, mafia__pb2.CommunicationResponse.FromString, options,
            channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
