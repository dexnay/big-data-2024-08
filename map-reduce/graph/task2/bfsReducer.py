#! /usr/bin/env python3

import sys

dict_graph = {}

for line in sys.stdin:
    v_input, weight, adjustment_string = line.strip().split('\t')
    adjustment_list = adjustment_string[1:-1].strip().split(',')
    if adjustment_list == ['']:
        adjustment_list = []
    if weight.strip() == 'INF':
        weight = float('inf')
    else:
        weight = int(weight)

    value = {"weight": weight, "adjustment_list": adjustment_list}

    if v_input not in dict_graph:
        dict_graph[v_input] = value
    else:
        if weight < dict_graph[v_input]['weight']:
            dict_graph[v_input]['weight'] = weight
        dict_graph[v_input]["adjustment_list"].extend(adjustment_list)

for key, value in dict_graph.items():
    weight = str(value['weight']).upper()
    adjustment_list = '{' + ','.join(value['adjustment_list']) + '}'
    print(f"{key}\t{weight}\t{adjustment_list}")


