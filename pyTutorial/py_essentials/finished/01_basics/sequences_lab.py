


# Make a list out of a string. Iterate or print the list to see the results.
l = list("hello world")
print l



# Using the set constructor function, how could you make a set of words?
# Print to prove the set is words and not letters.
s = set(["hello", "world"])
print s



# Make a list of 3 integers (what the integer values are is arbitrary).
# The following is safe in Python 2.
l2 = range(3)
print l2



# Turn that list into a tuple.
t = tuple(l2)
print t



# Compare the list and tuple. Why is the answer False when the values are
# the same?
print t == l2



# Unpack your list of integers and repack it into a new variable.
a, b, c = l2
t2 = a, b, c
print type(t2)
