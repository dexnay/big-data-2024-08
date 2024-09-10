#! /usr/bin/env python3

import sys

max_value = 0
min_value = 0
max_year = None
min_year = None
max_month = -1
min_month = -1

for line in sys.stdin:
    year, value = line.strip().split('\t')
    count, month = value.strip().split(',')
    count = int(count)

    if max_value <= count:
        max_value = count
        max_year = year
        max_month = int(month)
    if min_value >= count:
        min_value = count
        min_year = year
        min_month = int(month)

print(f"{max_year} {max_month} {max_value}")
print(f"{min_year} {min_month} {min_value}")