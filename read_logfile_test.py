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
        expected = "Sep 26 14:25:10 my-server-01 kernel: WARNING: CPU temperature is above safe threshold [12345]\n"
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