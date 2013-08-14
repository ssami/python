# Simple functions to play with NLTK

import nltk 
#from nltk.book import * 
from urllib import urlopen
import math

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
    allFreqs = sorted([text.count(w) for w in set(text)])
    print "sample", allFreqs[5:15]
    maxFreq = allFreqs[-1]
    print "max freq", maxFreq
    wordFreq = text.count(word)
    print "freq of word", wordFreq
    tf = 0.5 + (0.5 * wordFreq / maxFreq)
        
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
        tfidfList.append(tfidf)
        
    return tfidfList
   

def cleanText(url): 
    raw = urlopen(url).read()
    cleanHtml = nltk.clean_html(raw)
    tokens = nltk.word_tokenize(raw)
    text = nltk.Text(tokens)

    return text

 
