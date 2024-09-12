#! /usr/bin/env python3
"""Module providing a function task 4"""

import sys
import math

word_doc_count = {}
doc_word_count = {}
doc_count = set()

for line in sys.stdin:
    word, docname, tf, count = line.strip().split('\t')
    old_value = word_doc_count.get(word)
    if old_value is None:
        sum = int(count)
    else:
        sum = int(count) + old_value
    word_doc_count.update({word: sum})

    doc_count.update(docname)
    doc_word_count.update({(word, docname): tf})

for key, value in doc_word_count.items():
    word = key[0]
    docname = key[1]
    idf = math.log10(len(doc_count)/word_doc_count.get(word))
    print(f"{word}\t{docname}\t{value}\t{idf}")