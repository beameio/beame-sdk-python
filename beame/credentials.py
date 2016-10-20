import base64

import rsa

class Credentials:

    SIGNING_HASH = 'SHA-256'

    def __init__(self, fqdn=None, cert=None, private_key=None):
        self.fqdn = fqdn
        self.cert = cert
        self.private_key = private_key

    def need_field(self, attr, method):

        if not hasattr(self, attr):
            raise RuntimeError("beame.credentials.Credentials must have {} to {}()".format(attr, method))

    def sign(self, data):

        if not isinstance(data, bytes):
            raise ValueError("data must be bytes")

        self.need_field('fqdn', 'sign')
        self.need_field('private_key', 'sign')

        private_key = rsa.PrivateKey.load_pkcs1(self.private_key)

        message = {
            'signedData': data,
            'signedBy': self.fqdn,
            'signature': base64.b64encode(rsa.sign(data, private_key, self.SIGNING_HASH))
        }

        return message
