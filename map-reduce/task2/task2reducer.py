#! /usr/bin/env python3

import sys

result = {}

for line in sys.stdin:
    key, sum_input, count_input = line.strip().split('\t')
    old_value = result.get(key)
    if old_value is None:
        sum_result = int(sum_input)
        count = int(count_input)
    else:
        sum_result = int(sum_input) + old_value[0]
        count = old_value[1] + int(count_input)
    result.update({key:[sum_result, count]})

for key, value in result.items():
    avg = value[0]/value[1]
    print(f"{key} - {avg}")