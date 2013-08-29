import nltk_funcs
import nltk
import time
import sys
import re

def test1 (word): 
    print "Retrieving docs from online"
    t1 = time.time()
    holmes = nltk_funcs.cleanText('http://www.gutenberg.org/files/1661/1661-h/1661-h.htm')
    austen = nltk_funcs.cleanText('http://www.gutenberg.org/files/1342/1342-h/1342-h.htm')
    carroll = nltk_funcs.cleanText('http://www.gutenberg.org/files/11/11-h/11-h.htm')
    t2 = time.time()
    print "Done retrieving. Time taken (s): ", t2-t1
    
    print "Ranking..."
    t3 = time.time()
    rank = nltk_funcs.tfidf(word, texts=[holmes, austen, carroll])
    t4 = time.time()
    print "Done ranking. Time taken (s): ", t4-t3
    
    sortedTexts = []
    for tup in rank: 
        r, t = tup
        contexts = nltk_funcs.concordance(t, word)
        for c in contexts: 
            print " Found: ... ", c


def raw(file):
    contents = open(file).read()
    contents = re.sub(r'<.*?>', ' ', contents)
    contents = re.sub('\s+', ' ', contents)
    return contents

def test2(word):
    files = nltk.corpus.movie_reviews.abspaths()
    texts = []
    for f in files: 
        texts.append(nltk.Text(nltk.word_tokenize(raw(f))))
    rank = nltk_funcs.tfidf(word, texts)
    print rank[:5]

if __name__ == "__main__": 
    if len(sys.argv) > 1:
        search = sys.argv[1]        #get the word search arg
        test2(search)
    else: 
        print "Supply a word or phrase to search for"