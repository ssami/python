""" Python expresses functional and modular scope for variables.
"""


# Global to the module, not global in the builtin sense.
x = 5

def f1():
    """If not local, reference global.
    """
    x = 15
    return x

def f2():
    """Local references global.
    """
    global x
    x = 3
    return x


def f3():
	x = 100
	def f4():
		global x
		x = 25
	f4()
	return x

# Should print 5.
#print f1()
# Should print 3.
#print f2()
# Should print 3.
#print x

#print f3()
#print x


for i in range(10):
	pass

#print i 


# When done, open the python interpreter and import this module.
# Note the output when importing.
# Note that our "global" x is only available via reference of scope.x.
