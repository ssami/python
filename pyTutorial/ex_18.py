def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2) 

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2) 
	
print_two("First", "Second")

print_two_again("First two", "Second two")

