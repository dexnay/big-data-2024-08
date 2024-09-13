#! /usr/bin/env python3

import sys

ALFA = 0.1
N = 5

prev_node = None
sum_page_rank = 0
prev_adjacency = []

for line in sys.stdin:
    v_input, page_rank, adjustment_string = line.strip().split('\t')
    adjustment_list = adjustment_string[1:-1].strip().split(',')
    if adjustment_list == ['']:
        adjustment_list = []

    if not prev_node:
        if adjustment_string == '{}':
            sum_page_rank = float(page_rank)
        else:
            prev_adjacency = adjustment_list
    elif v_input == prev_node:
        if adjustment_string == '{}':
            sum_page_rank += float(page_rank)
        else:
            prev_adjacency = adjustment_list
    else:
        if prev_adjacency == []:
            page_rank = ALFA / N
        else:
            page_rank = ALFA / N + (1-ALFA)*sum_page_rank
        print(f"{prev_node}\t{page_rank}\t" + "{" + ','.join(prev_adjacency) + '}')

        if adjustment_string == '{}':
            sum_page_rank = float(page_rank)
        else:
            prev_adjacency = adjustment_list
            sum_page_rank = 0

    prev_node = v_input

if prev_node:
    if prev_adjacency == []:
        page_rank = ALFA / N
    else:
        page_rank = ALFA / N + (1 - ALFA) * sum_page_rank
    print(f"{prev_node}\t{page_rank}\t" + "{" + ','.join(prev_adjacency) + '}')



