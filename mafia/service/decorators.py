import mafia_pb2
import mafia.service.service_config as config


def validate_day(func):
    def wrapper(self, *args, **kwargs):
        if self._day_interval == config.DAY_INTERVAL.day:
            return func(self, *args, **kwargs)
        else:
            return mafia_pb2.Response(
                status=mafia_pb2.StatusCode.StatusCode_FORBIDDEN,
                message=f"You cannot perform that action during night")

    return wrapper


def validate_night(func):
    def wrapper(self, *args, **kwargs):
        if self._day_interval == config.DAY_INTERVAL.night:
            return func(self, *args, **kwargs)
        else:
            return mafia_pb2.Response(
                status=mafia_pb2.StatusCode.StatusCode_FORBIDDEN, message=f"You cannot perform that action during day")

    return wrapper


def validate_game_started(func):
    def wrapper(self, *args, **kwargs):
        if self._is_game_started:
            return func(self, *args, **kwargs)
        else:
            return mafia_pb2.Response(
                status=mafia_pb2.StatusCode.StatusCode_FORBIDDEN,
                message=f"You cannot perform that when game is not started")

    return wrapper


def validate_game_not_started(func):
    def wrapper(self, *args, **kwargs):
        if not self._is_game_started:
            return func(self, *args, **kwargs)
        else:
            return mafia_pb2.Response(
                status=mafia_pb2.StatusCode.StatusCode_FORBIDDEN,
                message=f"You cannot perform that when game is already started")

    return wrapper


def validate_is_alive(func):
    def wrapper(self, *args, **kwargs):
        request = args[0]
        if self._roles[request.user_id] != config.ROLES.ghost:
            return func(self, *args, **kwargs)
        else:
            return mafia_pb2.Response(
                status=mafia_pb2.StatusCode.StatusCode_FORBIDDEN,
                message=f"You cannot perform that action, as you are ghost")

    return wrapper


def validate_is_game(func):
    def wrapper(self, *args, **kwargs):
        if not self._is_game_finished:
            return func(self, *args, **kwargs)
        else:
            return mafia_pb2.Response(
                status=mafia_pb2.StatusCode.StatusCode_FORBIDDEN, message=f"Game has already finished")

    return wrapper


def lock(func):
    def wrapper(self, *args, **kwargs):
        with self._lock:
            return func(self, *args, **kwargs)

    return wrapper
