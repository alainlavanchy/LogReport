#!/usr/bin/env python3
"""LogReport Generator

This script takes a log file as input and generates two reports from the logs.
-> An error log
-> A usage log, showing how often each user has used the service.

Used modules:
-> re - to search for the entries in the logfile using regex
-> logging - to log errors
-> os - handle the files
"""

import re
import logging
import os


def read_logfile(file):
    if not isinstance(file, str):
        logging.error('Filename and path has to be a string.')
        exit(1)
    if not os.path.isfile(file):
        logging.error('File not found')
        exit(1)
    log_file = open(file, "r")
    print("File read")
    return log_file

def read_errors(file_object):
    error_log = {}
    Lines = file_object.readlines()
    for line in Lines:
        print(line)
        x = re.search(r"(ERROR:)(.*)(\([\w.]+\))", line)
        if (x):
            print(x.groups())
        else:
            print("Found nothing")
    return error_log

def read_usage(file):
    usage_log = {}
    return usage_log

def write_usage_csv(usage_logs, usage_csv_file):
    return

def write_error_csv(error_logs, error_csv_file):
    return

def main():
    logging.basicConfig(filename='LR_Logging.log', level=logging.INFO)
    logging.info('Start Logging')
    file = ('testlog.log')
    #Run the main code
    file_object = read_logfile(file)
    find_errors = read_errors(file_object)
    logging.info('End Logging')

if __name__ == "__main__":
    main()