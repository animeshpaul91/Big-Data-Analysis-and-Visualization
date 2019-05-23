#!/usr/bin/env python
"""A more advanced Mapper, using Python iterators and generators."""

import sys
import re

#wctop10 = ['first','year','said','team','player','basebal','leagu','one','season','game']
#wctop10 = ['kerr','year','game','team','basketbal','coach','play','olson','season','said']
#wctop10 = ['leagu','player','game','team','footbal','coach','kaepernick','year','season','said']
#wctop10 = ['tackl','coach','said','new','game','footbal','rugbi','leagu','player','play', 'year', 'team']

wctop10 = ['book','la','wire','de','com','diagram','page','que','date','doc']
#wctop10 = ['base', 'use','custom','pro','sie','boat','technolog','n','shop','cover']
#wctop10 = ['les', 'nn','vous','que','refriger','ale','de','rr','des','repair']

#wctop10 = ['jag', 'pdf','cancer','hiab','kebaya','volum','och','rr','hidden','att']

def main(inp):
    data = inp.read()
    paras = re.split(r'\n{2,}', data) #List of Paragraphs defined as a article's neighbourhood
    for para in paras:
        para = str(para)
        para = para.strip()
        words = para.split() #Number of words in the paragraph
        n = len(words)
        for i in range(0, n-1):
            if (words[i] in wctop10):
                for j in range(i+1, n):
                    print ('%s-%s\t%s' %(words[i], words[j], 1))
    
if __name__ == "__main__":
    main(sys.stdin)
