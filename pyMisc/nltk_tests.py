import nltk_funcs
import time

def test1 (word): 
    print "Retrieving docs from online"
    t1 = time.time()
    holmes = nltk_funcs.cleanText('http://www.gutenberg.org/files/1661/1661-h/1661-h.htm')
    austen = nltk_funcs.cleanText('http://www.gutenberg.org/files/1342/1342-h/1342-h.htm')
    carroll = nltk_funcs.cleanText('http://www.gutenberg.org/files/11/11-h/11-h.htm')
    t2 = time.time()
    print "Done retrieving. Time taken: ", t2-t1
    
    print "Ranking..."
    t3 = time.time()
    rank = nltk_funcs.tfidf(word, texts=[holmes, austen, carroll])
    t4 = time.time()
    print "Done ranking. Time taken: ", t4-t3
     
    print sorted(rank)
