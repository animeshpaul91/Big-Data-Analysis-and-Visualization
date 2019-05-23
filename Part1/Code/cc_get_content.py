#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 19:13:41 2019

@author: animesh
"""

import requests
import eventlet
from bs4 import BeautifulSoup
eventlet.monkey_patch()

topics = ['baseball', 'basketball', 'rugby', 'football']
#topics = ['rugby']

for topic in topics:
    urlList = []
    url_file = './' + topic + '/' + topic + '_urls.txt'
    out_file = './' + topic + '/' + topic + '_out.txt'
    f2 = open(url_file, 'r+')
    while(f2.readline() != ''):
        c = f2.readline()
        c = c[:-1]
        if(c != ''):
            urlList.append(c)

    with open(out_file, "a+") as write_file1:
        for url in urlList:
            print(url)
            # with eventlet.Timeout(5):
            try:
                content = str(requests.get(url, timeout=5).content)
            except:
                continue
            print("After content fetch")
            soup = BeautifulSoup(content, features="html5lib")
            origText = ''
            for p in soup.find_all('p'):
                text = p.get_text()
                origText += text + "\n"
            print(origText)
            write_file1.write(origText + "\n")
