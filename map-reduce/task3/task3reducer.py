#! /usr/bin/env python3
"""Module providing a function task 3"""

import sys

result = {}

for line in sys.stdin:
    key, element = line.strip().split('\t')
    result_value = result.get(element)
    if result_value is None:
        result_value = set()
        result_value.add(key)
    else:
        result_value.add(key)
    result.update({element: result_value})

for key, value in result.items():
    print(f"{key}\t{len(value)}")