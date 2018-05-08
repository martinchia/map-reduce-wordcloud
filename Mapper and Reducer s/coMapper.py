# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 22:47:08 2018

@author: Marti
"""
import sys
import re
from nltk.stem import PorterStemmer
from io import open

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
    stemmer = PorterStemmer()
    fstop = open('stopwords.txt','r',encoding = 'utf-8')
    fwords = open('part-00000','r', encoding = 'utf-8')
    topwords = []
    l = fwords.readline()
    c = 0
    while(l and c<10):
        word,count = l.strip().split('\t')
        topwords.append(word)
        l = fwords.readline()
        c+=1
    
    stop = fstop.read().split(',')
    dic = {}
    for line in data:
        words = line.decode('utf-8').strip().split()
        for i in range(len(words)):
            if(re.match('http.*',words[i])):
                continue
            word = ''.join(re.findall(r'[0-9a-zA-Z]*', words[i]))
            if(word.isdigit()):
                continue
            word = stemmer.stem(word)
            if(stopWords(words[i],stop)):
                continue
            if(not(word in topwords)):
                continue
            neighbors = ((),)
            if(i>=1 and i<=len(words)-2 and len(words)>=3):
                neighbors = words[i-1].encode("utf-8"),words[i+1].encode("utf-8")
            elif(i == 0 and len(words)>=2):
                neighbors = words[i+1].encode("utf-8"),
            elif(i == len(words)-1 and len(words)>=2):
                neighbors = words[i-1].encode("utf-8"),
            for n in neighbors:
                if(type(n) != str):
                    continue
                if(re.match('http.*',n)):
                    continue
                n = ''.join(re.findall(r'[0-9a-zA-Z]*',n))
                if(n.isdigit()):
                    continue
                n = stemmer.stem(n)
                if(not stopWords(n,stop)):
                    try:
                        dic[word,n] += 1
                    except KeyError:
                        dic[word,n] = 1
    for i in dic:
        print "%s,%s\t%s" % (i[0],i[1],dic[i])

if __name__ == "__main__":
    main()