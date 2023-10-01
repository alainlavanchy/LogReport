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
    logging.info("File read {}".format(file))
    return log_file

def read_errors(file_object):
    error_log = []
    Lines = file_object.readlines()
    logging.info("Found {} lines in the log".format(len(Lines)))
    for line in Lines:
        x = re.search(r"(ERROR:)(.*)(\([\w.]+\))", line)
        if (x):
            error_log.append(x.groups())
        else:
            logging.info("Found nothing")
    logging.info(error_log)
    return error_log

def read_usage(file_object):
    usage_log = []
    Lines = file_object.readlines()
    logging.info("Found {} lines in the log".format(len(Lines)))
    for line in Lines:
        x = re.search(r"(INFO:)(.*)(\([\w.]+\))", line)
        if (x):
            usage_log.append(x.groups())
        else:
            logging.info("Found nothing")
    logging.info(usage_log)
    return usage_log

def write_usage_csv(usage_logs, usage_csv_file):
    if not isinstance(usage_logs, list):
        logging.error('Usage log has to be a list.')
        exit(1)
    if not isinstance(usage_csv_file, str):
        logging.error('CSV filename has to be a string.')
        exit(1)
    return

def write_error_csv(error_logs, error_csv_file):
    if not isinstance(error_logs, list):
        logging.error('Usage log has to be a list.')
        exit(1)
    return

def main():
    logging.basicConfig(filename='LR_Logging.log', level=logging.INFO)
    logging.info('Start Logging')
    file = ('testlog.log')
    #Run the main code
    file_object = read_logfile(file)
    file_object2 = read_logfile(file)
    find_usage = read_usage(file_object)
    find_errors = read_errors(file_object2)
    logging.info('End Logging')

if __name__ == "__main__":
    main()