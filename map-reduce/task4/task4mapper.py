#! /usr/bin/env python3
"""Module providing a function task 4"""

import sys
from collections import defaultdict

def stripe_to_str(stripe):
    result = []
    for element in stripe:
        result.append(str(element)+':'+str(stripe[element]))
    return ','.join(result)

for line in sys.stdin:
    items = line.strip().split(' ')
    result = {}
    for i in items:
        stripe = defaultdict(int)
        for j in items:
            if i != j:
                stripe[j] = 1
        result.update({i: stripe_to_str(stripe)})

    for key, value in result.items():
        print(f"{key}\t{value}")