""" Build a Hash class that inherits from the dict object.

Use the following doctest to test out the module and conform to the
expected interactions.

Some notes about implementation:

* init with variable arguments.
* Need to facilitate access between attribute notation and index notation.
* Iteration iterates the sorted values of the dictionary, not the keys.



>>> h = Hash(cat=1, dog=2)
>>> h.cat
1
>>> h["cat"]
1
>>> h.chicken
>>> len(h)
2

>>> h2 = Hash(chickens=32, birds=24, humans=0)
>>> h2.birds
24
>>> len(h2)
3
>>> for value in h2:
...     print value
0
24
32
"""




if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
