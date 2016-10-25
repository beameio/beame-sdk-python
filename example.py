import os
import sys

from beame import auth_token, credentials, store, session

FQDN = 'gq19atbodwco2hck.p2payp4q8f5ruo22.v1.d.beameio.net'
BASE_DIR = os.path.join('/home/ilya/.beame/v2', FQDN)

# ---------- Initialization code ----------

# http://stackoverflow.com/questions/7409780/reading-entire-file-in-python
def get_file(fname):
    with open(fname, 'r') as f:
        content = f.read()
    return content

signing_creds = credentials.Credentials(
    fqdn        = FQDN,
    public_key  = get_file(os.path.join(BASE_DIR, 'public_key.pem')),
    private_key = get_file(os.path.join(BASE_DIR, 'private_key.pem'))
)
store.add(signing_creds)

# ---------- Step 1: Create session id ----------

session_id = session.create()

# ---------- Step 2: Validate session and create token ----------

session_ok = session.validate(session_id)

if session_ok:
    token = auth_token.create('my optional arbitrary data', store.get(FQDN), ttl=300)
    print("Created token:", token)
else:
    raise RuntimeError("Session validation failed - not giving token")

# ---------- Step 3: Validate token ----------

print("Internal token validation")

try:
    data = auth_token.validate(token)
    print("Good signature, data:", data)
except ValueError as e:
    print("Bad signature:", e)
