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
    """
    Parameters:
    file (str): Path to the log file

    Returns:
    File object

    The function checks if the filename is a string and if the file is present.
    It opens the file in readable mode and returns the file object.
    """
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
    """
    Parameters:
    file_object (file): File object containing the log file

    Returns:
    error_log (list): The found errors in the log as a list of tuples.

    The function extracts all errors in the log file using regex. It returns the error mark, the actual error and the username assigned to the error.
    """
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
    """
    Parameters:
    file_object (file): File object containing the log file

    Returns:
    usage_log (list): The found usages in the log as a list of tuples.

    The function extracts all usage info marked with INFO:. The generates a list of tuples containing the INFO mark, the actual usage and the username of the user assigend to the action.
    """
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

def create_error_report(error_logs):
    """
    Parameters:
    error_logs (list): List containing all information on the errors in tuples.

    Returns:
    error_report (dict): Dictionary containing the statistics of the errors found in the log.

    The function generates a dictionary listing the error causes and counts them. Sorted by counts.
    """
    error_report = {}
    return error_report

def create_usage_report(usage_logs):
    """
    Parameters:
    file_object (file): File object containing the log file

    Returns:
    usage_log (list): The found usages in the log as a list of tuples.

    The function extracts all usage info marked with INFO:. The generates a list of tuples containing the INFO mark, the actual usage and the username of the user assigend to the action.
    """
    usage_report = {}
    return usage_report


def write_usage_csv(usage_logs, usage_csv_file):
    """
    Parameters:
    file_object (file): File object containing the log file

    Returns:
    usage_log (list): The found usages in the log as a list of tuples.

    The function extracts all usage info marked with INFO:. The generates a list of tuples containing the INFO mark, the actual usage and the username of the user assigend to the action.
    """
    if not isinstance(usage_logs, list):
        logging.error('Usage log has to be a list.')
        exit(1)
    if not isinstance(usage_csv_file, str):
        logging.error('CSV filename has to be a string.')
        exit(1)
    usage_freq = {}
    for usage in usage_logs:
        if usage[3] in usage_freq:
            usage_freq[usage[3]] += 1
        else:
            usage_freq[usage[3]] = 1
    print(usage_freq)
    return

def write_error_csv(error_logs, error_csv_file):
    """
    Parameters:
    file_object (file): File object containing the log file

    Returns:
    usage_log (list): The found usages in the log as a list of tuples.

    The function extracts all usage info marked with INFO:. The generates a list of tuples containing the INFO mark, the actual usage and the username of the user assigend to the action.
    """
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
    file_object.close()
    file_object2.close()
    logging.info('End Logging')

if __name__ == "__main__":
    main()