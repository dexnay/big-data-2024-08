#! /usr/bin/env python3
"""Module providing a function task 4"""

import sys

doc_all_count = {}
doc_word_count = {}

for line in sys.stdin:
    word, docname, count = line.strip().split('\t')
    old_value = doc_word_count.get((word,docname))
    if old_value is None:
        sum = int(count)
    else:
        sum = old_value + int(count)
    doc_word_count.update({(word, docname): sum})

    old_value = doc_all_count.get(docname)
    if old_value is None:
        sum = int(count)
    else:
        sum = old_value + int(count)
    doc_all_count.update({docname: sum})

for key, value in doc_word_count.items():
    word = key[0]
    docname = key[1]
    sum_nk = int(doc_all_count.get(docname))-int(value)
    tf = int(value)/sum_nk
    print(f"{word}\t{docname}\t{tf}")