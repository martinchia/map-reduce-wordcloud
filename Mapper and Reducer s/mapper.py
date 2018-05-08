# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 22:47:08 2018

@author: Marti
"""
import sys
import re
from nltk.stem import PorterStemmer

def stopWords(word,stop):
    stemmer = PorterStemmer()
    if word in stop:
        return True
    if word.lower() in stop:
        return True
    if stemmer.stem(word) in stop:
        return True
    return False
    
def main():    
    data = sys.stdin
    f = open('stopwords.txt','r')
    stop = f.read().split(',')
    dic = {}
    for line in data:
        words = line.strip().split()
        for word in words:
            if(re.match('http.*',word)):
                continue
            word = ''.join(re.findall(r'[0-9a-zA-Z]*', word))
            if(word.isdigit()):
                continue
            if(not stopWords(word,stop)):
                try:
                    dic[word] += 1
                except KeyError:
                    dic[word] = 1
    for i in dic:
        print "%s\t%s" % (i,dic[i])

if __name__ == "__main__":
    main()