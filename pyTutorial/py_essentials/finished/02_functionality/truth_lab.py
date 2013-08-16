""" A lab of the easiest sort: all about True and False.
"""



# Understand why the results below are not boolean, and why we get the
# results we do. Where could the following be useful?
print 1 and 2
print 1 or 2
print 0 or 2
print 0 and 2



# Write two ways of converting the number 42 to a boolean value.
print not not 42
print bool(42)



# Write an if check without len that will print a message if a tuple is
# empty.
t = ()
if not t:
	print "Tuple is empty."



# Write two equivalent statements that return a boolean result on whether 
# or not a variable is None.
a = None
print a == None
print a is None
