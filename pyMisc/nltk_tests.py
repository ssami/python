import nltk_funcs


def test1 (): 
    holmes = nltk_funcs.cleanText('http://www.gutenberg.org/files/1661/1661-h/1661-h.htm')
    austen = nltk_funcs.cleanText('http://www.gutenberg.org/files/1342/1342-h/1342-h.htm')
    carroll = nltk_funcs.cleanText('http://www.gutenberg.org/files/11/11-h/11-h.htm')
    rank = nltk_funcs.tfidf('Alice', texts=[holmes, austen, carroll])

    print rank 
