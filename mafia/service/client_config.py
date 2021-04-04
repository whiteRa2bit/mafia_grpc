from mafia.utils import create_namedtuple_instance

COMMAND_TYPES = create_namedtuple_instance(
    'command_types',
    get_users='GET_USERS',
    broadcast='BROADCAST',
    vote_finish_day='VOTE_FINISH_DAY',
    decision='DECISION',
    accuse='ACCUSE')
