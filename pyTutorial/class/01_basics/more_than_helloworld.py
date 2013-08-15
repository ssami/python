"""

This is my first module


"""

# comment comment comment

hi = "hello internetz"

print hi 

n = 42

try:  
	print hi + n 
except BaseException as err: 
	print err 

print "And this is another string"


print type(n)
print type(hi)
print type(n) == type(hi)
print type(None)

print None == None

print None == False

print type(False)

print False == 0


def increment(n=42): 
	if type(n) != int: 
		n = int(n)

	return n + 42

print increment()
print increment("42")
#print increment("42a")




li = []

for i in range(10):
	li.append(i)


print li[0], "is the first item" 
print len(li)
# print len(n)

if __name__ == "__main__":
	# is my script the main script? 
	import random 
	import sys
	for d in sys.path: 
		print d

	
	print random.randint(1, 50)
	print __name__ #this will be "__main__"






