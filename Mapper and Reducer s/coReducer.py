# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 14:25:32 2018

@author: Marti
"""

import sys
from nltk.stem import PorterStemmer
def main():
    data = sys.stdin
    stemmer = PorterStemmer()
    dic = {}
    for line in data:
        words,count = line.split("\t")
        pair = tuple(words.split(','))
        try:
            dic[pair] += int(count)
        except KeyError:
            dic[pair] = int(count)
    sortedKeys = sorted(dic, key=dic.get, reverse=True)
    for i in sortedKeys:
        print "%s,%s\t%s" % (i[0],i[1],dic[i])

if __name__ == "__main__":
    main()