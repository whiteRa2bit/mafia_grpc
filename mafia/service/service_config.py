from mafia.utils import create_namedtuple_instance

ROLES = create_namedtuple_instance(
    'roles', mafia='mafia', detective='detective', innocent='innocent', ghost='ghost', not_assigned='not_assigned')

DAY_INTERVAL = create_namedtuple_instance('day_interval', day='day', night='night')

MIN_USERS_NUM = 3
MAFIA_NUM = 1
