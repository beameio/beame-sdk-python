import os
import sys

from beame import auth_token, credentials, store

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

# ---------- Token creation code ----------

token = auth_token.create('my optional arbitrary data', store.get(FQDN), ttl=300)

print("Created token:", token)

# ---------- Token validation code ----------

print("Internal token validation")

try:
    data = auth_token.validate(token)
    print("Good signature, data", data)
except ValueError as e:
    print("Bad signature", e)

# ---------- Token validation code, for testing tokens with CLI ----------

if len(sys.argv) > 1:
    print("CLI token validation")
    token = sys.argv[1]
    try:
        data = auth_token.validate(token)
        print("Good signature, data:", data)
    except ValueError as e:
        print("Bad signature:", e)
