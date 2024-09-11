#! /usr/bin/env python3
"""Module providing a function task 3"""

import sys

for line in sys.stdin:
    key, values = line.strip().split('\t')
    values = values.split(',')
    for i in values:
        print(f"{key}\t{i}")