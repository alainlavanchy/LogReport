#!/usr/bin/env python3
"""
Unit test fo the read_logfile function
"""

from LogReport import read_logfile
import unittest

class TestOpenLogFile(unittest.TestCase):
    def test_file_not_exists(self):
        testcase = "NoSuchLogFile.log"
        with self.assertRaises(SystemExit) as cm:
            read_logfile(testcase)
        self.assertEqual(cm.exception.code, 1)

    def test_logfile_exists(self):
        testcase = "testlog.log"
        expected = "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (peter.marlow)\n"
        file = read_logfile(testcase)
        teststring = file.readline()
        file.close()
        self.assertEqual(teststring,expected)

    def test_filname_is_no_string(self):
        testcase = [0,1]
        with self.assertRaises(SystemExit) as dm:
           read_logfile(testcase)
        self.assertEqual(dm.exception.code, 1)

unittest.main(exit=False)