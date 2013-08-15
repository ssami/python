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

from collections import Counter

f = open("../testdocs/TaleOfTwoCities.txt", "r")
data = f.read().lower()

#print data[0:50]

words = data.split()

print "There are %d words in this book" % len(words)

uniques = set(words)

print "There are %s unqiue words in this book" % len(uniques)

#print words[:100]

word_counts = {}
for w in words: 
	if w in word_counts:
		word_counts[w] += 1
	else: 
		word_counts[w] = 1


keys = word_counts.keys()
values = word_counts.values()
items = word_counts.items()

sorted_items = sorted(items, reverse=True, key=lambda item: item[1])
print sorted_items[:10]

#print word_counts

import time
t1 = time.time()
print t1
print Counter(words).most_common(10)
t2 = time.time()
print t2
print "Time taken: ", t2-t1


print ""

for word, count in sorted_items[:10]: 
	print word, ": ", count
