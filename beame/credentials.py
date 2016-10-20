import base64

import rsa

class Credentials:

    SIGNING_HASH = 'SHA-256'

    def __init__(self, fqdn=None, public_key=None, private_key=None):
        self.fqdn = fqdn
        self.public_key = public_key
        self.private_key = private_key

    def need_field(self, attr, method):

        if not hasattr(self, attr):
            raise RuntimeError("beame.credentials.Credentials must have {} to {}()".format(attr, method))

    def sign(self, data):

        if not isinstance(data, bytes):
            raise ValueError("beame.credentials.Credentials.sign(): data must be bytes")

        self.need_field('fqdn', 'sign')
        self.need_field('private_key', 'sign')

        private_key = rsa.PrivateKey.load_pkcs1(self.private_key)

        message = {
            'signedData': str(data, 'UTF-8'),
            'signedBy': self.fqdn,
            'signature': str(base64.b64encode(rsa.sign(data, private_key, self.SIGNING_HASH)), 'UTF-8')
        }

        return message

    def check_signature(self, data):
        public_key = rsa.PublicKey.load_pkcs1(self.public_key)
        return rsa.verify(data['signedData'].encode('UTF-8'), base64.b64decode(data['signature']), public_key)
