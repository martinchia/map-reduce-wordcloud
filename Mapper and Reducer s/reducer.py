# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 22:47:08 2018

@author: Marti
"""

import sys
from nltk.stem import PorterStemmer
def main():
    data = sys.stdin
    stemmer = PorterStemmer()
    dic = {}
    for line in data:
        word,count = line.split("\t")
        word = stemmer.stem(word)
        try:
            dic[word] += int(count)
        except KeyError:
            dic[word] = int(count)
    sortedKeys = sorted(dic, key=dic.get, reverse=True)
    for i in sortedKeys:
        print "%s\t%s" % (i,dic[i])

if __name__ == "__main__":
    main()