#! /usr/bin/env python3
"""Module providing a function task 4"""

import sys
import re

for line in sys.stdin:
    docname, content = line.strip().split(':')
    content = re.sub(f'[^a-zA-Z0-9]', ' ', content)
    words = content.split(' ')
    for i in range(len(words)):
        print(f"{words[i]}\t{docname}\t1")