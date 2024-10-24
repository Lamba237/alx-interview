#!/usr/bin/python3
"""
Log parsing
"""


import sys
import re
import signal

# Initialize variables
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Regular expression to match the required log format
log_pattern = re.compile(r'^\S+ - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)$')

def print_statistics():
    """Print the collected statistics."""
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C)."""
    print_statistics()
    sys.exit(0)

# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Read lines from stdin
for line in sys.stdin:
    match = log_pattern.match(line.strip())
    if match:
        status_code = int(match.group(1))
        file_size = int(match.group(2))
        
        total_file_size += file_size
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
        
        line_count += 1
        if line_count % 10 == 0:
            print_statistics()

# Print statistics at the end if the script ends normally
print_statistics()