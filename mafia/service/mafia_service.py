import logging
import threading
import time
import random
from concurrent import futures

import grpc

import mafia_pb2
import mafia_pb2_grpc
import mafia.service.service_config as config
from mafia.service.decorators import validate_day, validate_night, validate_game_started, validate_game_not_started, \
    validate_is_alive, validate_is_game, lock


class MafiaServicer(mafia_pb2_grpc.MafiaServicer):
    def __init__(self):
        self._lock = threading.Lock()
        self._day_interval = config.DAY_INTERVAL.day
        self._users = {}  # {user_id: mafia_pb2_grpc.User}
        self._roles = {}  # {user_id: config.ROLES}
        self._accuse_votes = {}  # {accusing_user_id: accused_user_id}
        self._mafia_votes = {}  # {mafia_user_id: victim_user_id}
        self._detective_votes = {}  # {detective_user_id: suspect_user_id}
        self._user_messages = {}  # {user_id: ['message1', ...]}
        self._finish_day_votes = {}  # {user_id: True}
        self._is_game_started = False
        self._is_game_finished = False
        self._day_num = 0

    @validate_is_game
    def init_communication_channel(self, request_iterator, context):
        user_id = None
        while True:
            for request in request_iterator:
                user_id = request.user_id
                if request.data_type == mafia_pb2.CommunicationDataType.Value('HANDSHAKE_MESSAGE'):
                    print(f'Hanshake with user {user_id}')
                    yield self._handle_handshake_message()
                elif request.data_type == mafia_pb2.CommunicationDataType.Value('BROADCAST_MESSAGE'):
                    print(f'Received broadcast message from {user_id}')
                    yield self._handle_broadcast_message(request)
                elif request.data_type == mafia_pb2.CommunicationDataType.Value('DECISION_MESSAGE'):
                    print(f'Received mafia message from {user_id}')
                    yield self._handle_decision(request)
                elif request.data_type == mafia_pb2.CommunicationDataType.Value('EMPTY_MESSAGE'):
                    pass

            if user_id is not None and self._user_messages[user_id]:
                message = self._user_messages[user_id].pop(0)
                yield message
            else:
                yield mafia_pb2.CommunicationResponse()

    def _handle_handshake_message(self):
        return mafia_pb2.CommunicationResponse(message='You successfully joined Mafia game', author='Admin')

    @validate_is_alive
    def _handle_broadcast_message(self, request):
        cur_user_id = request.user_id
        message = request.message
        user_role = self._roles[cur_user_id]
        filter_role = lambda _: True

        if self._day_interval == config.DAY_INTERVAL.night:
            if user_role in [config.ROLES.mafia, config.ROLES.detective]:
                filter_role = lambda role: role == user_role
            else:
                return mafia_pb2.Response(
                    status=mafia_pb2.StatusCode.StatusCode_FORBIDDEN, message=f"You cannot message during night")
        for user_id in self._users:
            if cur_user_id != user_id and filter_role(self._roles[user_id]):
                self._user_messages[user_id].append(
                    mafia_pb2.CommunicationResponse(message=message, author=self._users[cur_user_id].name))
        return mafia_pb2.CommunicationResponse()

    @validate_night
    @validate_is_alive
    def _handle_decision(self, request):
        print(f"Decision request: {request}")
        print(f"Mafia votes: {self._mafia_votes}")
        print(f"Detective votes: {self._detective_votes}")
        cur_user_id = request.user_id
        role = self._roles[cur_user_id]
        if role in [config.ROLES.mafia, config.ROLES.detective]:
            target_user_id = int(request.message.strip())
            if target_user_id not in self._users:
                return mafia_pb2.CommunicationResponse(message=f'No user with id {target_user_id}', author='Admin')
            elif (role == config.ROLES.mafia and self._mafia_votes[cur_user_id] is not None) or \
                (role == config.ROLES.detective and self._detective_votes[cur_user_id] is not None):
                return mafia_pb2.CommunicationResponse(message='You already voted', author='Admin')
            elif self._roles[target_user_id] == role:
                return mafia_pb2.CommunicationResponse(
                    message=f'User {target_user_id} has the same role with you', author='Admin')
            elif self._roles[target_user_id] == config.ROLES.ghost:
                return mafia_pb2.CommunicationResponse(message=f'User {target_user_id} is already died', author='Admin')
            else:
                if role == config.ROLES.mafia:
                    votes = self._mafia_votes
                elif role == config.ROLES.detective:
                    votes = self._detective_votes
                else:
                    raise ValueError("Invalid role")

                votes[cur_user_id] = target_user_id
                for user_id in self._users:
                    if user_id != cur_user_id and self._roles[user_id] == role:
                        self._user_messages[user_id].append(
                            mafia_pb2.CommunicationResponse(
                                message=f'I vote for {target_user_id}', author=self._users[cur_user_id].name))
                return mafia_pb2.CommunicationResponse(message=f"You voted for user {target_user_id}", author='Admin')
        else:
            return mafia_pb2.CommunicationResponse(message="You are not mafia or detective", author='Admin')

    @validate_game_not_started
    @lock
    @validate_is_game
    def add_user(self, request, context):
        print(f'User messages: {self._user_messages}')
        cur_user_id = len(self._users)
        name = request.name
        while cur_user_id in self._users:
            cur_user_id += 1

        for user_id in self._users:
            self._user_messages[user_id].append(
                mafia_pb2.CommunicationResponse(message=f'User {name} has just been added', author='Admin'))

        user = mafia_pb2.User(user_id=cur_user_id, name=name)
        self._users[cur_user_id] = user
        self._roles[cur_user_id] = config.ROLES.not_assigned
        self._user_messages[cur_user_id] = []

        return mafia_pb2.Response(status=mafia_pb2.StatusCode.StatusCode_CREATED, data={"user_id": str(cur_user_id)})

    @validate_game_not_started
    @validate_is_game
    def delete_user(self, request, context):
        user_id = request.user_id
        if user_id in self._users:
            del self._users[user_id]
            return mafia_pb2.DeleteUserResponse(status=mafia_pb2.StatusCode.StatusCode_OK)
        else:
            return mafia_pb2.Response(
                status=mafia_pb2.StatusCode.StatusCode_NOT_FOUND, message=f"No user with id {user_id}")

    def _is_alive(self, user_id):
        return self._roles[user_id] != config.ROLES.ghost

    def get_users(self, request, context):
        users = '\n'.join([
            f'{user.name}, user_id: {user.user_id}, is alive: {self._is_alive(user.user_id)}'
            for user in self._users.values()
        ])
        return mafia_pb2.Response(status=mafia_pb2.StatusCode.StatusCode_OK, data={"users": users})

    @lock
    def _assign_roles(self):
        assert len(self._users) >= config.MIN_USERS_NUM

        shuffled_user_ids = random.sample(self._users.keys(), len(self._users))
        mafias_num = config.MAFIA_NUM

        for user_id in shuffled_user_ids[:mafias_num]:
            self._roles[user_id] = config.ROLES.mafia

        self._roles[shuffled_user_ids[mafias_num]] = config.ROLES.detective

        for user_id in shuffled_user_ids[mafias_num + 1:]:
            self._roles[user_id] = config.ROLES.innocent

    @validate_day
    @validate_game_started
    @validate_is_alive
    @validate_is_game
    def accuse_user(self, request, context):
        if self._day_num > 1:
            accusing_user_id = request.accusing_user_id
            accused_user_id = request.accused_user_id

            if self._roles[accused_user_id] == config.ROLES.ghost:
                return mafia_pb2.Response(
                    status=mafia_pb2.StatusCode.StatusCode_BAD_REQUEST,
                    message=f'User {accused_user_id} is already a ghost')
            elif accusing_user_id in self._users and accused_user_id in self._users:
                self._accuse_votes[accusing_user_id] = accused_user_id
                return mafia_pb2.Response(status=mafia_pb2.StatusCode.StatusCode_OK, message='OK')
            else:
                return mafia_pb2.Response(status=mafia_pb2.StatusCode.StatusCode_BAD_REQUEST, message='Wrong user ids')
        else:
            return mafia_pb2.Response(
                status=mafia_pb2.StatusCode.StatusCode_BAD_REQUEST, message="You can't vote in the first day")

    def run(self):
        print("Run")
        while True:
            if not self._is_game_started and len(self._users) >= config.MIN_USERS_NUM:
                self._start_game()
            if self._is_game_started:
                # Finish day and start night
                if all(self._finish_day_votes.values()) and self._day_interval == config.DAY_INTERVAL.day:
                    self._start_night()

                # Start day
                elif all([x is not None for x in self._mafia_votes.values()]) and all(
                    [x is not None for x in self._detective_votes.values()]) and \
                        self._day_interval == config.DAY_INTERVAL.night:
                    print("Everybody voted, finish night")
                    self._start_day()

                elif self._is_mafia_win() and not self._is_game_finished:
                    self._is_game_finished = True
                    for user_id in self._user_messages:
                        mafias = [
                            user.name
                            for user in self._users.values()
                            if self._roles[user.user_id] == config.ROLES.mafia
                        ]
                        self._user_messages[user_id].append(
                            mafia_pb2.CommunicationResponse(message=f'Mafia ({mafias}) wins!', author='Admin'))

    @lock
    def _is_mafia_win(self):
        alive_mafia_count = 0
        alive_others_count = 0
        for user_id in self._users:
            if self._is_alive(user_id):
                if self._roles[user_id] == config.ROLES.mafia:
                    alive_mafia_count += 1
                else:
                    alive_others_count += 1
        return alive_mafia_count >= alive_others_count

    def _start_game(self):
        print("Started game")
        self._is_game_started = True
        self._assign_roles()
        self._start_day()
        print("Game started")
        for user_id in self._users:
            self._user_messages[user_id].append(
                mafia_pb2.CommunicationResponse(
                    message=f'Game has just started, your role is {self._roles[user_id]}', author='Admin'))

    @validate_day
    @validate_game_started
    @validate_is_alive
    @validate_is_game
    @lock
    def vote_finish_day(self, request, context):
        cur_user_id = request.user_id
        print(f"Received VOTE for DAY FINISH from {cur_user_id}")
        if cur_user_id in self._users:
            self._finish_day_votes[cur_user_id] = True
            for user_id in self._users:
                if user_id != cur_user_id:
                    self._user_messages[user_id].append(
                        mafia_pb2.CommunicationResponse(
                            message=f'User {cur_user_id} voted to finish game day', author='Admin'))
            return mafia_pb2.Response(status=mafia_pb2.StatusCode.StatusCode_OK, message='Your vote has been counted')
        else:
            return mafia_pb2.Response(status=mafia_pb2.StatusCode.StatusCode_BAD_REQUEST, message='Wrong user id')

    @lock
    def _start_day(self):
        print("Started day")
        assert len(self._users) >= config.MIN_USERS_NUM
        if self._day_num != 0:
            self._execute_mafia_decision()
            self._execute_detective_decision()

        self._day_interval = config.DAY_INTERVAL.day
        self._day_num += 1
        self._accuse_votes = {
            user_id: None for user_id in self._users if self._roles[user_id] is not config.ROLES.ghost
        }
        self._finish_day_votes = {
            user_id: False for user_id in self._users if self._roles[user_id] is not config.ROLES.ghost
        }

    def _execute_mafia_decision(self):
        mafia_votes = list(self._mafia_votes.values())
        target_user_id = max(set(mafia_votes), key=mafia_votes.count)
        self._roles[target_user_id] = config.ROLES.ghost

        for user_id in self._users:
            if user_id == target_user_id:
                message = mafia_pb2.CommunicationResponse(message='Mafia killed you', author='Admin')
            else:
                message = mafia_pb2.CommunicationResponse(message=f'Mafia killed user {target_user_id}', author='Admin')
            self._user_messages[user_id].append(message)

    def _execute_detective_decision(self):
        detective_votes = list(self._detective_votes.values())
        target_user_id = max(set(detective_votes), key=detective_votes.count)

        if self._roles[target_user_id] == config.ROLES.mafia:
            self._roles[target_user_id] = config.ROLES.ghost
            for user_id in self._users:
                self._user_messages[user_id].append(
                    mafia_pb2.CommunicationResponse(
                        message=f'Detective found mafia: user {target_user_id}', author='Admin'))
        else:
            for user_id in self._users:
                self._user_messages[user_id].append(
                    mafia_pb2.CommunicationResponse(message=f'Detective didnt find mafia', author='Admin'))

    @lock
    def _start_night(self):
        print("Started night")
        if self._day_num != 1:
            self._kill_accused_user()
        self._mafia_votes = {user_id: None for user_id in self._users if self._roles[user_id] == config.ROLES.mafia}
        self._detective_votes = {
            user_id: None for user_id in self._users if self._roles[user_id] == config.ROLES.detective
        }
        self._day_interval = config.DAY_INTERVAL.night
        self._finish_day_votes = {user_id: False for user_id in self._users}
        for user_id in self._users:
            self._user_messages[user_id].append(
                mafia_pb2.CommunicationResponse(message=f'Night started', author='Admin'))
            if self._roles[user_id] == config.ROLES.mafia:
                self._user_messages[user_id].append(
                    mafia_pb2.CommunicationResponse(message=f'Choose who to kill', author='Admin'))
            elif self._roles[user_id] == config.ROLES.detective:
                self._user_messages[user_id].append(
                    mafia_pb2.CommunicationResponse(message=f'Choose who to check', author='Admin'))

    def _kill_accused_user(self):
        votes = list(self._accuse_votes.values())
        target_user_id = max(set(votes), key=votes.count)
        self._roles[target_user_id] = config.ROLES.ghost

        for user_id in self._users:
            if user_id == target_user_id:
                message = mafia_pb2.CommunicationResponse(
                    message='Majority voted for you, you are a ghost now', author='Admin')
            else:
                message = mafia_pb2.CommunicationResponse(
                    message=f'User {target_user_id} was killed by votes', author='Admin')
            self._user_messages[user_id].append(message)


def serve(servicer):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mafia_pb2_grpc.add_MafiaServicer_to_server(servicer, server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    servicer = MafiaServicer()
    threads = [threading.Thread(target=lambda: serve(servicer)), threading.Thread(target=lambda: servicer.run())]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
