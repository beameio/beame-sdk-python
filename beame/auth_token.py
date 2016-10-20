import json
import time
import beame.credentials

# __all__ = ['create']

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
    
    # token = base64.b64encode(token)
    token = json.dumps(token).encode()

    return signing_creds.sign(token)
