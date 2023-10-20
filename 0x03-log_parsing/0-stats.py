#!/usr/bin/python3

import sys
import re
from collections import defaultdict
import signal

# Define the regular expression pattern to match the log line format
log_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+) - \[([^\]]+)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)')

# Initialize variables and data structures to store metrics
total_size = 0
status_code_counts = defaultdict(int)
lines_processed = 0

# Function to print the metrics
def print_metrics():
    print("Total file size: File size:", total_size)
    for status_code in sorted(status_code_counts.keys()):
        print(f"{status_code}: {status_code_counts[status_code]}")

# Function to handle keyboard interruption (CTRL + C)
def signal_handler(signal, frame):
    print_metrics()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Read lines from stdin and process them
for line in sys.stdin:
    # Use the regular expression pattern to match the log line format
    match = log_pattern.match(line)
    if match:
        ip_address, _, status_code, file_size = match.groups()
        status_code = int(status_code)
        file_size = int(file_size)

        total_size += file_size
        status_code_counts[status_code] += 1
        lines_processed += 1

        # Print metrics after processing every 10 lines
        if lines_processed % 10 == 0:
            print_metrics()

print_metrics()

