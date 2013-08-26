# Make a list out of a string. Iterate or print the list to see the results.
s = "hello world"
li = list(s)
for c in li: 
	print c, 

print ''
print "Printing with join: ", ' '.join(li)
print li

# Using the set constructor function, how could you make a set of words?
# Print to prove the set is words and not letters.
words = ['hi', 'this', 'is', 'a', 'class']
st = set(s)
print st
print len(st), "is the length"

st2 = set(words)
print st2
print len(st2), "is the length"

for item in st2: 
	print item 

for item in st: 
	print item 


# Make a list of 3 integers (what the integer values are is arbitrary).
# The following is safe in Python 2.
num = [1, 2, 3]

print num

num2 = list((1, 2, 3))
print num2

# Turn that list into a tuple.

t = tuple(num2) 

print t


# Compare the list and tuple. Why is the answer False when the values are
# the same?

print num2 == t

# Unpack your list of integers and repack it into a new variable.

a, b, c = t
print "Unpacked..."
print a
print b
print c

v = a, b, c
print "Repacked ", v


# Random number generators
# Build list of hundred random numbers from random import randint
# Add numbers in list to get a total value

from random import randint

lis = []
total = 0
for i in range(100): 
	r = randint(1, 100)
	lis.append(r)
	total += r

print total 
print lis


# list comprehension!

lis2 = [randint(1, 100) for n in range(100)]

print "List comprehension: ", lis2

print "Summing automatically: ", sum(lis2)


# Opening file

f = open('text.txt', 'w')
f.write("Hi this is a file write!")
for n in lis2: 
	f.write(str(n) + "\n")

f.close()


f = open("text.txt", "r")
for line in f: 
	print line

print "Printing with with..."

with open("text.txt", "r") as f: 
	for line in f: 
		print line



f.close()


