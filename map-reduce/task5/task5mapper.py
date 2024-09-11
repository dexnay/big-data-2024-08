#! /usr/bin/env python3
"""Module providing a function task 4"""

import sys

for line in sys.stdin:
    user_id, value = line.strip().split('\t')
    if 'query' in value:
        print(f"{user_id}\t{value.split(':')[1]}\t*")
    else:
        print(f"{user_id}\t*\t{value.split(':')[1]}")