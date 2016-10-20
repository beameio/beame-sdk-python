#!/usr/bin/env python

import os
import unittest

from beame import auth_token, credentials, store

e = os.environ

class TokenTestCase(unittest.TestCase):

    DATA = 'abc123!@#'
    ENV_ENCODING='ascii'

    def setUp(self):
        self.signing_creds = credentials.Credentials(
            fqdn        = e['FQDN'],
            public_key  = e['PUBLIC_KEY'],
            private_key = e['PRIVATE_KEY']
        )
        store.add(self.signing_creds)

    def testCreateValidate(self):
        token = auth_token.create(self.DATA, self.signing_creds, ttl=300)
        print('*** TOKEN CREATED', token)
        data = auth_token.validate(token)
        print('*** TOKEN VALIDATE DATA', data)


if __name__ == "__main__":
    unittest.main()
