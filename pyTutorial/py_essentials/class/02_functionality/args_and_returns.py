

def compare(x=1, y=1):
	return x == y


compare2 = lambda x, y: x == y 


print compare(1, 1)
print compare(2, 1)

print compare(1, 1)

print compare(3)

print compare(y=3) 

print compare(y=3, x=3)


"""
Variable number of unlabeled numbers

"""
def summary(*numbers):
	print "numbers is %s elements long" % len(numbers) 
	return sum(numbers) 

print summary(1, 2, 3, 1000, 10, 34)

print "Passing a range of numbers created on the fly..."
print summary(*range(20))

print "You need to deref them or you get an error..."
try:
	summary(range(20))
except BaseException as err: 
	print err


def test(x, y=3, *numbers):
	pass


test(1)
test(1, 2)
test(1, 2, 3)
#try: 
#	test(x=1, y=2, 3)
#except BaseException as err: 
#	print err


def keyval(**keyargs):
	if "dog" not in keyargs: 
		keyargs["dog"] = "woof"; 
	for key, val in keyargs.items(): 
		print key, val



keyval(key="skeleton", cat="meow")