#! /usr/bin/env python3

import sys

for line in sys.stdin:
    print(line.strip())
    v_input, page_rank, adjustment_string = line.strip().split('\t')
    adjustment_list = adjustment_string[1:-1].strip().split(',')
    p = float(round(float(page_rank)/len(adjustment_list), 3))
    p = "%.3f" % p
    if adjustment_list != ['']:
        for node in adjustment_list:
            print(f'{node}\t{p}\t' + '{}')