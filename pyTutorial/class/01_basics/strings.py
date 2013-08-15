s = "this is normal" 

s2 = 'this is normal'

s3 = r"this is a \n raw string with escape"
s1 = "this is a \n raw string without escape" 

print s3
print s1


#sprintf tokenized output

print "%s is a %s" % ("chicken", "bird")

print "%d is also %s" % (42, 42)

print "With formatting: " , "{0} is a {1}" .format("chicken", "bird")


if __name__ == "__main__":
	#message = raw_input("What is your message? ")
	#with open("messages.txt", "a") as f: 
	#	f.write(message + "\n")

	#with open("messages.txt", "r") as f: 
	#	for line in f: 
	#		print "message previously delivered: %s" % (line.rstrip())


	import re

	s = "HI there i'm a string"
	email = r"This is my email: sumita_sami@gmail.com"

	print re.findall("hi", s, re.I)
	print re.findall(r"\w+", s)

	print re.findall(r"\w+@\w+\.\w+", email)
