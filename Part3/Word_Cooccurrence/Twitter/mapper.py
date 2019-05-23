#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import sys

#wctop10 = ['basebal','criptocurr', 'ohtanicoin', 'game', 'bet', 'amp', 'mlb', 'sport', 'shoheiohtani', 'baseballplay']
#wctop10 = ['grade','th', 'ncaa', 'nba', 'sport', 'def', 'basketbal', 'boy', 'game', 'tournament']
#wctop10 = ['daihyo','urawar', 'hike', 'gtnfl', 'footbal', 'sport', 'yoga', 'jleagu', 'run', 'soccer']
wctop10 = ['un','le', 'en', 'la', 'el', 'rugbi', 'match', 'sport', 'de', 'los']

def main(inp):
    for line in inp:
        line = line.strip()
        words = line.split()
        n = len(words)
        for i in range(0, n-1):
            if (words[i] in wctop10):
                for j in range(i+1, n):
                    print ('%s-%s\t%s' %(words[i], words[j], 1))

if __name__ == "__main__":
    main(sys.stdin)
