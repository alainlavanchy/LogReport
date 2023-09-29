"""LogReport Generator

This script takes a log file as input and generates two reports from the logs.
-> An error log
-> A usage log, showing how often each user has used the service.

Used modules:
-> re - to search for the entries in the logfile using regex
"""

import re