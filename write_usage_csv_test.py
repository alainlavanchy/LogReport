#!/usr/bin/env python3
"""
Unit test for the write_usage_csv function
"""

from LogReport import write_usage_csv
import unittest

class TestWriteUsageCSV(unittest.TestCase):
    def test_usage_logs_is_not_list(self):
        usage_log = 123
        with self.assertRaises(SystemExit) as cm:
            write_usage_csv(usage_log, 'usage_report.csv')
        self.assertEqual(cm.exception.code, 1)

    def test_filename_not_string(self):
        usage_log = ['Error','12']
        logfile = []
        with self.assertRaises(SystemExit) as cm:
            write_usage_csv(usage_log, logfile)
        self.assertEqual(cm.exception.code, 1)

unittest.main(exit=False)