#!/bin/bash
# Define the variables
logfile="testlog.log"
error_report="errer_report.csv"
usage_report="usage_report.csv"

# Change to the directory
cd /path/to/script

# Run the report script
python LogReport.py $logfile

# Run the csv to html conversion
python Conversion.py $error_report error_report.html
python Conversion.py $usage_report usage_report.html

# Move the files to the correct directory
mv usage_report.html ~/documents
mv error_report.html ~/documents

