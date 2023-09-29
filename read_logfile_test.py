#!/usr/bin/env python3
"""
Unit test fo the read_logfile function
"""

from LogReport import read_logfile
import unittest

class TestOpenLogFile(unittest.TestCase):
    def test_file_not_exists(self):
        testcase = "NoSuchLogFile.log"
        expected = None
        self.assertEqual(read_logfile(testcase), expected)


unittest.main()