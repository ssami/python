# Simple functions to play with NLTK

import nltk 
#from nltk.book import * 
import requests
import string
import math
from collections import Counter
import re

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
    #allFreqs = sorted([text.count(w) for w in set(text)])
    count_common = Counter(text).most_common(1)
    w, maxFreq = count_common[0]
    #print "max freq", maxFreq
    wordFreq = text.count(word)
    #print "freq of word", wordFreq
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
        tfidfList.append(tfidf)
        
    return tfidfList
   

def cleanText(url): 
    raw = requests.get(url).text
    cleanHtml = nltk.clean_html(raw)
    noPunc = re.sub("[\.\t\,\:;\(\)\.]", "", cleanHtml, 0, 0)
    # noPunc = cleanHtml.translate(None, string.punctuation)
    tokens = nltk.word_tokenize(noPunc)
    text = nltk.Text(tokens)

    return text

 
 
 
 # 1. get from URL (urlopen)
 # 2. clean up html (nltk.clean_html)
 # 3. clean up punctuation (<text>.translate(None, string.punctuation))
 # 4. tokenize (nltk.word_tokenize(text))
 # 5. run through counter (Counter(text).most_common(10))
 #
 #



 
