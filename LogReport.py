#!/usr/bin/env python3
"""LogReport Generator

This script takes a log file as input and generates two reports from the logs.
-> An error log, showing all the error messages sorted by their frequency.
-> A usage log, showing how often each user has used the service and how many errors he forced.

Used modules:
-> re - to search for the entries in the logfile using regex
-> logging - to log errors
-> os - handle the files
-> csv - to create the csv files
"""

import re
import logging
import os
import csv



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
    error_logs (list): List containing all information on the errors, in tuples.

    Returns:
    error_report (dict): Dictionary containing the statistics of the errors found in the log.

    The function generates a dictionary listing the error causes and counts them. Sorted by counts.
    """
    error_report = {}
    for errors in error_logs:
        error_message = errors[1][1:-1]
        if error_message in error_report:
            error_report[error_message] += 1
        else:
            error_report[error_message] = 1
    myKeys = list(error_report.keys())
    myKeys.sort()
    error_report_sorted = {i: error_report[i] for i in myKeys}
    logging.info(error_report_sorted)
    return error_report_sorted

def create_usage_error_report(usage_logs, error_logs):
    """
    Parameters:
    usage_logs (list): List containing all information on the usage, in tuples.
    error_logs (list): List containing all information on the errors, in tuples

    Returns:
    usage_report (dict): Dictionary containing the statistics of the usage information found in the log.

    The function generates a dictionary listing the usage of the script by user. Sorted by counts.
    """
    usage_report = {}
    for usage in usage_logs:
        username = usage[2]
        username = username[1:-1]
        if username in usage_report:
            usage_report[username]["usage"] += 1
        else:
            usage_report[username] = {}
            usage_report[username]["usage"] = 1
            usage_report[username]["errors"] = 0
    for errors in error_logs:
        username = errors[2]
        username = username[1:-1]
        if username in usage_report:
            if "errors" in usage_report[username]:
                usage_report[username]["errors"] += 1
            else:
                usage_report[username]["errors"] = 1
        else:
            usage_report[username] = {}
            usage_report[username]["errors"] = 1
            usage_report[username]["usage"] = 0
    myKeys = list(usage_report.keys())
    myKeys.sort()
    usage_report_sorted = {i: usage_report[i] for i in myKeys}
    logging.info(usage_report_sorted)
    return usage_report_sorted


def write_usage_csv(usage_report, usage_csv_file):
    """
    Parameters:
    usage_report (dict): Dictonary containg the information on the usage of the script
    usage_csv_file (str): The filename of the csv file to be created.

    Returns:
    Nothing

    The function creates a csv file, using the information in the dictionary.
    """
    if not isinstance(usage_report, dict):
        logging.error('Usage report has to be a dictionary.')
        exit(1)
    if not isinstance(usage_csv_file, str):
        logging.error('CSV filename has to be a string.')
        exit(1)

    #Defining the fields for the csv columns
    fields = ["Username", "Usage", "Errors"]

    #Opening the csv file
    with open (usage_csv_file, "w", newline="") as csv_file:
        #Create the csv writer
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()
        usernames = list(usage_report.keys())
        for username in usernames:
            line = {}
            line["Username"] = username
            line["Errors"] = usage_report[username]["errors"]
            line["Usage"] = usage_report[username]["usage"]
            writer.writerow(line)
    logging.info("CSV Report {} created".format(usage_csv_file))
    return

def write_error_csv(error_report, error_csv_file):
    """
    Parameters:
    error_report (dict): Dictonary containg the information on the errors of the script
    error_csv_file (str): The filename of the csv file to be created.

    Returns:
    Nothing

    The function creates a csv file, using the information in the dictionary.
    """
    if not isinstance(error_report, dict):
        logging.error('Error report has to be a dictionary.')
        exit(1)

    if not isinstance(error_csv_file, str):
        logging.error('CSV filename has to be a string.')
        exit(1)
    #Defining the fields for the csv columns
    fields = ["Error", "Counts"]

    #Opening the csv file
    with open (error_csv_file, "w", newline="") as csv_file:
        #Create the csv writer
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()
        errors = list(error_report.keys())
        for error in errors:
            line = {}
            line["Error"] = error
            line["Counts"] = error_report[error]
            writer.writerow(line)
    logging.info("CSV Report {} created".format(error_csv_file))
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
    usage_report = create_usage_error_report(find_usage, find_errors)
    error_report = create_error_report(find_errors)
    file_object.close()
    file_object2.close()
    write_error_csv(error_report, "error_report.csv")
    write_usage_csv(usage_report, "usage_report.csv")
    logging.info('End Logging')

if __name__ == "__main__":
    main()