#!/usr/bin/python3
import sys


total_size = 0  # Initialize the total file size to 0

# Store the count of all status codes in a dictionary
status_count = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                '404': 0, '405': 0, '500': 0}

count = 0  # Keep count of the number lines counted

try:
    for line in sys.stdin:
        line_list = line.split(" ")

        # Check if the line follows the expected format
        if len(line_list) > 4:
            status_code = line_list[-2]
            file_size = int(line_list[-1])

            # Check if the status code received exists in the dictionary
            # and increment its count
            if status_code in status_count.keys():
                status_count[status_code] += 1

            # Update total size
            total_size += file_size

            # Update count of lines
            count += 1

        # If count reaches 10, print statistics and reset count
        if count == 10:
            count = 0  # Reset count
            print('File size: {}'.format(total_size))

            # Print status code counts
            for key, value in sorted(status_count.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    # Print final statistics after loop completion or interruption
    print('File size: {}'.format(total_size))
    for key, value in sorted(status_count.items()):
        if value != 0:
            print('{}: {}'.format(key, value))