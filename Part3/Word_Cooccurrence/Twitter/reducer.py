#!/usr/bin/env python
"""A more advanced Reducer, using Python iterators and generators."""

import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word_pair, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue
    
    if current_word == word_pair:
        current_count += count
    else:
        if current_word:
            print ('%s\t%s' %(current_word, current_count))
        current_count = count
        current_word = word_pair

if current_word == word_pair:
    print ('%s\t%s' %(current_word, current_count))

