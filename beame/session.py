import collections
import random
import string
import time

DEFAULT_SESSION_ID_LENGTH = 32
DEFAULT_SESSION_ID_TTL = 10

issued_session_ids = collections.OrderedDict()
characters = string.ascii_uppercase + string.digits

__all__ = ['create', 'validate', 'cleanup']


def create(ttl=DEFAULT_SESSION_ID_TTL, session_id_length=DEFAULT_SESSION_ID_LENGTH):
    session_id = ''.join(random.SystemRandom().choice(characters) for _ in range(session_id_length))
    issued_session_ids[session_id] = int(time.time()) + ttl
    return session_id


def _delete(session_id):
    del issued_session_ids[session_id]


def validate(session_id):
    cleanup()
    now = int(time.time())
    if session_id in issued_session_ids:
        ok = issued_session_ids[session_id] >= now
        _delete(session_id)
        return ok
    return False


def cleanup():
    now = int(time.time())
    to_delete = []
    for k, v in issued_session_ids.items():
        if v < now:
            to_delete.append(k)
        else:
            break
    for k in to_delete:
        _delete(k)

if __name__ == "__main__":
    sess = create(ttl=-1)
    print(len(issued_session_ids))
    print(validate(sess))
    print(len(issued_session_ids))
