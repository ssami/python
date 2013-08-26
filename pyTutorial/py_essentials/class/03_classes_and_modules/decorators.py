# Closure!

def increase(f):
	def wrapper(x):
		return f(x) + 42
	return wrapper


#print echo(42)
#echo2 = increase(echo)



class Empty(object):
	@property
	def x(self): 
		return 42

#
#e = Empty()
#print e.x

@increase
@increase
@increase
def echo(x): 
	return x

print echo(42)