"""
    Lab:
    ----

    Using testdocs/TaleOfTwoCities.txt:

    * Count the number words in the book.
    * Figure out the top ten most used words.

    Hints:
    
    Word count should be ~135k
    Check out Counter in the Python docs.
"""

import re
from collections import Counter

if __name__ == "__main__":
    print "Counting number of words in the book."

    try:
        book = open("../testdocs/TaleOfTwoCities.txt", "r")
    except IOError as err:
        print "File error:", err
        exit(err.errno)

    count = 0
    counter = re.compile(r"\w+(?:-{1})?\w+", re.I)
    # Counters are extended dictionaries.
    wordcounts = Counter()

    for line in book:
        words = counter.findall(line)
        count += len(words)
        for word in words:
            # Don't treat title, upper, and lower case words differently.
            wordcounts[word.lower()] += 1

    print "Total words:", count
    
    print "Top 10 most used words:"
    for word, count in wordcounts.most_common(10):
        print word, count
    
    # or all the words (counter is an extended dictionary).
    #for word, count in wordcounts.items():
    #    print word, count
    
    # Clean up.
    book.close()
