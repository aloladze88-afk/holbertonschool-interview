#!/usr/bin/python3
"""Log parsing script."""

import re
import sys


def print_stats(total_size, status_counts):
    """Print the total file size and status code counts."""
    print("File size: {}".format(total_size))

    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))


def main():
    """Read stdin line by line and compute log metrics."""
    total_size = 0
    line_count = 0

    valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]
    status_counts = {code: 0 for code in valid_codes}

    pattern = re.compile(
        r'^\S+ - \[.*\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'
    )

    try:
        for line in sys.stdin:
            match = pattern.match(line.strip())

            if not match:
                continue

            status_code = int(match.group(1))
            file_size = int(match.group(2))

            total_size += file_size
            line_count += 1

            if status_code in status_counts:
                status_counts[status_code] += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise

    print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
