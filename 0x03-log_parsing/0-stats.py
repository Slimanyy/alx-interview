#!/usr/bin/python3
"""
    a script that reads stdin line by line and computes metrics
"""
import sys


if __name__ == '__main__':
    # variables to store metrics
    total_file_size = 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    processed_line = 0
    statistics = {}
    for code in codes:
        statistics[code] = 0

    def print_statistics(statistics: dict, total_file_size: int):
        print('File size: {}'.format(total_file_size))
        for code, count in sorted(statistics.items()):
            if count:
                print("{}: {}".format(code, count))

    try:
        for line in sys.stdin:
            processed_line += 1
            data = line.split()
            try:
                status_code = data[-2]
                if status_code in statistics:
                    statistics[status_code] += 1
            except BaseException:
                # skip line if status code isn't in the correct position
                pass
            try:
                file_size = int(data[-1])
                total_file_size += file_size
            except BaseException:
                # skip line if status code isn't in the correct position
                pass

            #  print statistics After every 10 lines
            if processed_line % 10 == 0:
                print_statistics(statistics, total_file_size)
        print_statistics(statistics, total_file_size)
    except KeyboardInterrupt:
        #  print final statistics if the keyboard is interrupted (control C)
        print_statistics(statistics, total_file_size)
        raise
