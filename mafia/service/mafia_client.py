import os
import logging
import random
import threading

import grpc

import mafia_pb2
import mafia_pb2_grpc
import mafia.service.client_config as config
from mafia_pb2 import User, AddUserRequest, BaseUserRequest, StatusCode


class MafiaClient():
    def __init__(self):
        self.name = input('Enter your name: ')
        with grpc.insecure_channel('localhost:50051') as channel:
            self.stub = mafia_pb2_grpc.MafiaStub(channel)
            self.user_id = self.add_user()
            self.lock = threading.Lock()
            self.messages = [
                mafia_pb2.CommunicationRequest(
                    user_id=self.user_id, data_type=mafia_pb2.CommunicationDataType.Value('HANDSHAKE_MESSAGE')),
            ]
            threads = [
                threading.Thread(target=lambda: self.server_communication()),
                threading.Thread(target=lambda: self.cli_communication())
            ]
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()

    def add_user(self):
        response = self.stub.add_user(AddUserRequest(name=self.name))
        user_id = response.data['user_id']
        return int(user_id)

    def cli_communication(self):
        self.cli_in_process = False
        while True:
            if not self.cli_in_process:
                command = input("> ")
                self._execute_command(command)
                self.cli_in_process = False

    def server_communication(self):
        def generate_messages():
            if self.messages:
                message = self.messages.pop(0)
                yield message
            else:
                yield mafia_pb2.CommunicationRequest(
                    user_id=self.user_id, data_type=mafia_pb2.CommunicationDataType.Value('EMPTY_MESSAGE'))

        while True:
            try:
                responses = self.stub.init_communication_channel(generate_messages())
                for response in responses:
                    if response.message or response.author:
                        print(f"{response.author}: {response.message}", end='\n> ')
                    else:
                        break
            except:
                print("Game finished")
                os._exit(0)

    def _execute_command(self, command_str):
        command_str = command_str.strip()
        if not command_str:
            return
        command = command_str.split()[0]
        args_str = ' '.join(command_str.split()[1:])

        if command == config.COMMAND_TYPES.get_users:
            response = self.stub.get_users(mafia_pb2.Empty())
            print(response.data['users'])
        elif command == config.COMMAND_TYPES.broadcast:
            message = args_str
            self.messages.append(
                mafia_pb2.CommunicationRequest(
                    user_id=self.user_id,
                    message=message,
                    data_type=mafia_pb2.CommunicationDataType.Value('BROADCAST_MESSAGE')))
        elif command == config.COMMAND_TYPES.vote_finish_day:
            response = self.stub.vote_finish_day(mafia_pb2.BaseUserRequest(user_id=self.user_id))
            print(response)
        elif command == config.COMMAND_TYPES.decision:
            target_str_id = args_str.strip()
            self.messages.append(
                mafia_pb2.CommunicationRequest(
                    user_id=self.user_id,
                    message=target_str_id,
                    data_type=mafia_pb2.CommunicationDataType.Value('DECISION_MESSAGE')))
        print(f"Executed {command}")


if __name__ == '__main__':
    logging.basicConfig()
    client = MafiaClient()
