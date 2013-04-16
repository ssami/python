import sys

def test_valid_string (string) : 
	if string is None : 
		print "String is null object." 
		return False
			
	elif not string : 
		print "This is an empty string" 
		return False
	else : 
		print "This string has something *%s*" % (string) 
		return True


## Can also ask for user input in command line
args_length = len(sys.argv)
if (args_length != 2) : 
	print "Usage: python object_check_suite.py <string args>" 
else :
	str_arg = sys.argv[1]
	print str_arg
	test_valid_string(str_arg)