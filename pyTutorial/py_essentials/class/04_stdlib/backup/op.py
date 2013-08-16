#op.py

import sys
import os
from subprocess import * 

#check existence of file or directory

#Usage: 
# python [myscript] path 


f = open("testfile", "w")
f.write("This is a random string!")
f.close()


def filestats(path):
	if os.path.exists(path): 
		print "Yes,", path, "exists"
		print "Is a file", os.path.isfile(path)
		print "Is a dir", os.path.isdir(path)
		stdout = check_output(["cat", path])
		print "This file has characters %s characters" % len(stdout)

		if os.path.isfile(path):
			return True

	return False



if len(sys.argv) > 1: 
	for arg in sys.argv: 
		print "You passed arg: ", arg
	path = sys.argv[1]; 	
else: 
	path = raw_input("What file do you want to get stats on? ")

while(True):
	if filestats(path):
		r = raw_input("Do you want to remove this file? ")
		if r[:1].lower() == 'y': 
			os.remove(path) 
	else: 
		print "Nope,", path, "doesn't exist"

	command = raw_input("Another path or 'quit'")
	#if command[:1] == 'q': 
	if command.lower() == "quit": 
		break
	else: 
		path = command
