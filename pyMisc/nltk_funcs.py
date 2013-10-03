# Simple functions to play with NLTK

import nltk 
#from nltk.book import * 
import requests
import string
import math
from collections import Counter
import re

from nltk.text import ConcordanceIndex

from searchDoc import Document


def lexical_diversity(text):
    """Calculates lexical diversity by dividing the number of unique words by the total number of words"""
    numWords = len(text)
    uniqueWords = len(set(text))
        
    return uniqueWords / numWords


def word_frequency(text, word):
    """Calculates the frequency of this word in the text"""
    wordCount = text.count(word)
    frequency = wordCount / len(text) * 100
    
    return frequency

def character_words(text, wordLen=10, fDist=7):
    """Words that reflect the character of a text"""
    vocab = set(text)
    fdist = FreqDist(text)
    characList = [word for word in vocab if len(word)>10 and fdist[w]>7]
    
    return charactList
    
def tf_text(text, word):
    # tf = 0.5 + (0.5 * rawfreq(word, text)/max{raw freq of any word in text})
    # idf = log (total num of docs / num docs with term)
    count_common = Counter(text).most_common(1)
    w, maxFreq = count_common[0]
    wordFreq = text.count(word)
    tf = (0.5 * wordFreq / maxFreq)
        
    return tf
        
def tfidf(word, texts=[]):         
    numTextsWithWord = 0
    for t in texts:
        if t.count(word) > 0:
            numTextsWithWord += 1
    idf = math.log(float(len(texts)) / float(numTextsWithWord))
    tfidfList = []
    for t in texts:
        tfidf = tf_text(t, word) * idf
        tfidfList.append((tfidf, t))
        
    return sorted(tfidfList, reverse=True)
   

def cleanText(url): 
    raw = requests.get(url).text
    cleanHtml = nltk.clean_html(raw)
    noPunc = re.sub("[\.\t\,\:;\(\)\.\'\"]", "", cleanHtml, 0, 0)
    # noPunc = cleanHtml.translate(None, string.punctuation)
    tokens = nltk.word_tokenize(noPunc)
    text = nltk.Text(tokens)

    return text


def concordance(text, word):
    cindex = ConcordanceIndex(text, key=lambda x:x.lower())
    offsetList = cindex.offsets(word)
    contexts = []
    for i in offsetList[:10]:
        pre = i-10
        post = i+10
        contextStr = ' '.join(text[pre:post])
        contexts.append(contextStr)
    return contexts
 

def loadIndex():
    fh = open('index.txt', 'r')
    index = {}
    terms = fh.readlines()
    for l in terms: 
        l = l.rstrip()
        divs = l.split(":")
        term = divs[0]
        docs = divs[1].split(",")
        index[term] = docs
    
    fh.close()
    return index

def writeIndex(index): 
    fh = open('index.txt', 'w')
    for t, d in index.items(): 
        doclist = ','.join(d)
        line = t + ':' + doclist
        fh.write(line)
        

def prepText(url):
    raw = requests.get(url).text
    result = re.findall('<title>(.*)</title>', raw, flags=re.I|re.M|re.S)
    title = result[0]
    cleanHtml = nltk.clean_html(raw)
    noPunc = re.sub("[\.\t\,\:;\(\)\.\'\"]", "", cleanHtml, 0, 0)
    doc = Document(title, noPunc)
    
    return doc
    

def addToIndex(searchdoc):
    # Append to index
    from nltk.corpus import stopwords
    sw = stopwords.words('english')
    
    tokens = nltk.word_tokenize(searchdoc.body)
    index = loadIndex()
    for w in set(tokens): 
        if w not in sw:
            if w in index: 
                index[w].append(searchdoc.title)
            else:   
                index[w] = list()
                index[w].append(searchdoc.title)
     
    writeIndex(index)
            
    