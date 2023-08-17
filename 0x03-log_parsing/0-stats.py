import sys
import signal

status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
status_count = {code: 0 for code in status_codes}
total_file_size = 0
line_count = 0

def print_statistics():
    print(f"Total file size: File size: {total_file_size}")
    for code in sorted(status_codes):
        if status_count[code] > 0:
            print(f"{code}: {status_count[code]}")

def process_line(line):
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
