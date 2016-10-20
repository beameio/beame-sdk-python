#!/usr/bin/env python

import os
import unittest

from beame import auth_token, credentials

e = os.environ

class TokenTestCase(unittest.TestCase):

    DATA = 'abc123!@#'
    ENV_ENCODING='ascii'

    def setUp(self):
        self.signing_creds = credentials.Credentials(
            fqdn        = e['FQDN'],
            cert        = e['CERT'],
            private_key = e['PRIVATE_KEY']
        )

    def testCreateValidate(self):
        token = auth_token.create(self.DATA, self.signing_creds, ttl=300)
        print(token)


if __name__ == "__main__":
    unittest.main()
