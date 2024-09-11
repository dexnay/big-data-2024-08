#! /usr/bin/env python3
"""Module providing a function task 4"""

import sys

result = {}

for line in sys.stdin:
    key, value = line.strip().split('\t')
    H = {}
    for element in value.split(','):
        a,b = element.split(':')
        H.update({a: b})

    for k,v in H.items():
        old_value = result.get((key,k))
        if old_value is None:
            result.update({(key, k): int(v)})
        else:
            result.update({(key, k): int(v)+old_value})

for key, value in result.items():
    print(f"{key}\t{len(value)}")