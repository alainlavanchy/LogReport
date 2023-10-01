#!/usr/bin/env python3
"""
Unit test fo the read_errors function
"""

from LogReport import read_errors
import unittest

class TestOpenLogFile(unittest.TestCase):
    def test_object_is_not_a_string(self):
        testfile = 123
        with self.assertRaises(SystemExit) as cm:
            read_errors(testfile)
        self.assertEqual(cm.exception.code, 1)

    def test_find_error(self):
        teststring ="Sep 26 14:27:05 my-server-01 apache2[56789]: [error] AH00124: Request exceeded limit of 10 internal redirects due to probable configuration error"
        
unittest.main(exit=False)