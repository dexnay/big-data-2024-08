#! /usr/bin/env python3
"""Module providing a function task 4"""

import sys

old_user = None
queries = []
urls = []

for line in sys.stdin:
    user_id, query, url = line.strip().split('\t')
    if  old_user != user_id:
        if old_user is not None:
            print(f"{old_user}\t{queries}\t{urls}")
        old_user = user_id
        if query == '*':
            queries = []
        else:
            queries = [query]
        if url =='*':
            urls = []
        else:
            urls = [url]
    else:
        if url !='*':
            urls.append(url)
        if query != '*':
            queries.append(query)

if old_user is not None:
    print(f"{old_user}\t{queries}\t{urls}")