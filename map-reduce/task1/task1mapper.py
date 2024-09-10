#! /usr/bin/env python3

import sys

for line in sys.stdin:
    input_data = line.strip().split('  ')
    year = input_data[0]
    data = input_data[1:-1]
    for month in range(len(data)):
        value = data[month]
        print(f"{year}\t{value},{month}")