from sys import argv

script, filename = argv

print "We're going to erase $%r" % filename
print "If you don't want that, hit CTRL-C."
print "If you do want that, hit RETURN"
raw_input("?")

print "Opening the file..." 
target = open (filename, 'w')
print "Truncating the file. Bye!"
#target.truncate()

print "Going to write to file!"

target.write("Test1\n")
target.write("Test2\n")

print "Closing and leaving"
target.close()

