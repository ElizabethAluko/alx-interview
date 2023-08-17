#!/usr/bin/env python3

import sys
import signal

def print_metrics(metrics):
    total_size = sum(metrics.values())
    print(f"Total file size: File size: {total_size}")
    for status_code in sorted(metrics.keys()):
        print(f"{status_code}: {metrics[status_code]}")

def main():
    metrics = {}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.strip().split()

            if len(parts) != 10:
                continue

            ip, _, _, date, _, _, request, status_code, file_size = parts
            if not status_code.isdigit():
                continue

            status_code = int(status_code)
            file_size = int(file_size)

            metrics[status_code] = metrics.get(status_code, 0) + 1

            if status_code in {200, 301, 400, 401, 403, 404, 405, 500}:
                metrics[status_code] = metrics.get(status_code, 0) + 1

            line_count += 1

            if line_count % 10 == 0:
                print_metrics(metrics)

    except KeyboardInterrupt:
        print_metrics(metrics)
        sys.exit(0)

if __name__ == "__main__":
    main()
