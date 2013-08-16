"""Not to be confused with the collections library, Python includes a set
of builtin collections.

Review of the basic collection types and some common functionality.

Strings are sequences, too, but we'll cover them separately and more in
depth.

"""


# Lists: mutable, mixedtype arrays.
# Semantics: lists are (often) more powerful when the data contained within
# are homogeneous.
l = [1, 2, 3]
# How many items?
print len(l)
# 0-based index.
print l[0]
# Mutable, but array boundaries enforced.
try:
    l[3] = "hi there"
except IndexError as err:
    print "oops, error:", err
# Can construct lists from any iterable, including strings.
letters = list("abc")
# We can enumerate a list as well as just iterate over it.
# The following technique also demonstrates unpacking. We'll see more 
# packing/unpacking as time goes on.
for i, letter in enumerate(letters):
    print i, letter
# Push an item onto our list.
l.append(4)
# Insert (index, value).
l.insert(0, 0)
print "Our list l:", l
# Remove items from our list.
print "Pop last item:", l.pop()
print "Shift first item:", l.pop(0)
print "Our list now has length:", len(l)
# We can check for the presence of items:
print "Is the number 2 in our list?", 2 in l
# Another way to remove items at a particular index: the del keyword
del l[1]
print "Is the number 2 in our list?", 2 in l
print "How many items are left?", len(l)
print "Our list:", l



# Tuples: immutable list-like structures.
# Very similar to lists, but being immutable, their semantics, while not
# strictly enforced, can be powerful. (A coordinate on the globe is easily,
# semantically expressed as a simple tuple.)

# Two ways to create an equivalent tuple.
t = (1, 2, 'hello')
t2 = 1, 2, 'hello'
# Python supports shallow comparisons between tuples (and lists).
print "Is t and t2 equal?", t == t2
print "t has {} elements".format(len(t))
# Can read...
print "Item at index 0:", t[0]
# ...but can't write.
try:
    t[0] = 1000
except TypeError as err:
    print "Nope, can't change it. Got error:", err
# Tuples, acting as a semantic package, can be unpacked into equivalent
# number of variable.
a, b, c = t
print "a:", a
print "b:", b
print "c:", c
# Syntax for a single element tuple.
# No.
t3 = ("hello")
# Yes (trailing comma).
t4 = ("hello",)
print "t3 has type:", type(t3)
print "t4 has type:", type(t4)



# Python mutable dictionary types provide unique key access.
# Keys can be any immutable type.
# Values can be any Python type.
d = {"chickens": 2, "cats": 5, None: 1000}
# Access.
print "How many have cats:", d["cats"]
print "How many have None:", d[None]
# Mutate on the fly.
d["dogs"] = 10
# dictionaries are iterable.
print "How many items in our dict?", len(d)
# Can iterate on the key in the dictionary.
for k in d:
    print k, d[k]
# dictionaries have a nice iterator helper.
for k, v in d.items():
    print k, v
# Tests against keys, not values.
print "Is cats in our dict?", "cats" in d



# Sets: mutable list of distinct items.
# This literal notation is relatively new.
s = {1, 1, 1, 2, 3, 4}
print "What is in my set?", s
# Original set constructor.
s2 = set([4, 5, 6, 7])
print "Intersection of sets:", s & s2
print "Union of sets:", s | s2
# Mutable sets can be added to. Need to pass an iterable in.
s.update([5])
print "Intersection of sets:", s & s2
