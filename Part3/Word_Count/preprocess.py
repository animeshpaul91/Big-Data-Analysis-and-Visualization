#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 02:58:55 2019

@author: animesh
"""
import re
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
stemmer = SnowballStemmer("english", ignore_stopwords=True)
stop_words = set(stopwords.words('english'))

def process_tweets(files):
    emojis = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        "]+", flags=re.UNICODE)
    for file in files:
        f1 = open("./Input/"+file+".txt", "r")
        f2 = open("./Processed/Twitter/"+file+"_tw.txt", "a+")
        for line in f1:
            line = ' '.join(re.sub("([0-9]+)|(@[A-Za-z0-9]+)|([^A-Za-z0-9 \t])|(\w+:\/\/\S+)"," ", line).split()) #Removes Hashtags, @, URLS
            line = emojis.sub(r'',line) #Remove Emojis
            words = line.split()
            stemmed_words = [stemmer.stem(word) for word in words] #Stemming
            final_words = [word for word in stemmed_words if word not in stop_words] #Removing stopwords
            out = ' '.join(final_words) #Convert List to string
            f2.write(out+"\n")
    f2.close()
    f1.close()


def process_nyt(files):
    for file in files:
        f1 = open("./Input/"+file+"_content.txt", "r")
        f2 = open("./Processed/NYT/"+file+"_nyt.txt", "a+")
        for line in f1:
            line = ' '.join(re.sub('([0-9]+)|([^A-Za-z]+)',' ', line).split())
            words = line.split()
            stemmed_words = [stemmer.stem(word) for word in words] #Stemming
            final_words = [word for word in stemmed_words if word not in stop_words] #Removing stopwords
            out = ' '.join(final_words) #Convert List to string
            f2.write(out+"\n")
    f2.close()
    f1.close()
    
    
def process_sc(files):
    for file in files:
        f1 = open("./Processed/NYT/"+file+"_nyt.txt", "r")
        f2 = open("./Processed/NYT/"+file+"_nyt_out.txt", "a+")
        for line in f1:
            line = re.sub('(xe\sx\sx\s)','',line)
            f2.write(line)
    f2.close()
    f1.close()
    
def process_cc(files):
    for file in files:
        f1 = open("./Input/"+file+"_out.txt", "r")
        f2 = open("./Processed/CC/"+file+"_cc.txt", "a+")
        for line in f1:
            #line = re.sub('(\\\\x..)','',line)
            line = ' '.join(re.sub('([0-9]+)|([^A-Za-z]+)',' ', line).split())
            words = line.split()
            stemmed_words = [stemmer.stem(word) for word in words] #Stemming
            final_words = [word for word in stemmed_words if word not in stop_words] #Removing stopwords
            out = ' '.join(final_words) #Convert List to string
            f2.write(out+"\n")
    f2.close()
    f1.close()
    
def process_sc1(files):
    for file in files:
        f1 = open("./Processed/CC/"+file+"_cc.txt", "r")
        f2 = open("./Processed/CC/"+file+"_cc_out.txt", "a+")
        for line in f1:
            line = re.sub('(x[a-z]*)','',line)
            line = re.sub('(\s[a-z]\s)','',line)
            line = re.sub('(\s[a-z]\s)','',line)
            line = re.sub('(\s[a-z][a-z]\s)','',line)
            line = re.sub('(\s[a-z][a-z]\s)','',line)
            line = re.sub('(^n\s)','',line)
            f2.write(line)
    f2.close()
    f1.close()

if __name__ == "__main__":
    files = ["baseball", "basketball", "football", "rugby"]
    process_nyt(files)
    process_tweets(files)
    process_sc(files)
    process_cc(files)
    process_sc1(files)
