import json
import time

import beame.credentials
import beame.common_utils
import beame.store

TIME_FUZZ = 5 # Seconds

__all__ = ['create', 'validate']

def create(data, signing_creds, ttl=10):

    if not isinstance(signing_creds, beame.credentials.Credentials):
        raise ValueError("signing_creds must be instance of beame.credentials.Credentials")

    if not isinstance(data, str):
        raise ValueError("data must be a string")

    now = int(time.time())

    token = {
        'created_at': now,
        'valid_till': now + ttl,
        'data': data
    }

    token = json.dumps(token).encode('UTF-8')

    return json.dumps(signing_creds.sign(token))

def validate(token):
    auth_token = beame.common_utils.parse(token)
    # print("*** AUTH TOKEN", auth_token)

    if not isinstance(auth_token, dict):
        raise ValueError("auth_token must be a dict. Token passed to validate() is probably in invalid format.")

    for k in 'signedData', 'signedBy', 'signature':
        if k not in auth_token:
            raise ValueError("token has no .{}".format(k))

    if not isinstance(auth_token['signedData'], str):
        raise ValueError("auth_token signedData must be a string")

    creds = beame.store.get(auth_token['signedBy'])
    signature_ok = creds.check_signature(auth_token)
    # print("*** SIGNATURE_OK", signature_ok)
    if not signature_ok:
        raise ValueError("Bad signature")

    signed_data = beame.common_utils.parse(auth_token['signedData'])

    now = int(time.time())

    if signed_data['created_at'] > now + TIME_FUZZ:
        raise ValueError("created_at is in future - invalid token or incorrect clock")

    if signed_data['valid_till'] < now - TIME_FUZZ:
        raise ValueError("valid_till is in the past - token expired")

    return auth_token
