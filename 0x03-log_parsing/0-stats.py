#!/usr/bin/python3

"""
This script reads input from stdin line by line, processes each line according to the specified format,
and computes and prints metrics such as total file size and number of lines by status code.
"""

import sys
import signal

status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
status_count = {code: 0 for code in status_codes}
total_file_size = 0
line_count = 0

def print_statistics():
    """
    Print statistics including total file size and number of lines by status code.
    """
    print(f"Total file size: File size: {total_file_size}")
    for code in sorted(status_codes):
        if status_count[code] > 0:
            print(f"{code}: {status_count[code]}")

def process_line(line):
    """
    Process a single line and update metrics accordingly.
    
    :param line: The input line to process.
    """
    global total_file_size, line_count
    parts = line.split()
    if len(parts) != 10:
        return

    ip, _, _, _, _, request, status, size = parts[0], parts[5], parts[8], parts[9]
    if status not in status_codes:
        return

    try:
        size = int(size)
    except ValueError:
        return

    status_count[status] += 1
    total_file_size += size
    line_count += 1

    if line_count % 10 == 0:
        print_statistics()

try:
    for line in sys.stdin:
        process_line(line.strip())
except KeyboardInterrupt:
    print("\nKeyboard interruption detected. Printing statistics:")
    print_statistics()
