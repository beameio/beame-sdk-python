#!/usr/bin/env python

import os
import unittest

from beame.session import *

class TokenTestCase(unittest.TestCase):

    def testExpiredSession(self):
        sess = create(ttl=-1)
        self.assertEqual(len(sess), 32)
        self.assertFalse(validate(sess))

    def testGoodSession(self):
        sess = create(ttl=2)
        self.assertTrue(validate(sess))


if __name__ == "__main__":
    unittest.main()
