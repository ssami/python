from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file: %r : " % filename
print txt.read()

print "Type the filename again: " 
file_again = raw_input("> ")
txt_again = open(file_again)
 
count = 0
for line in txt_again: 
	count += 1
	print "%d: %s" % (count, line),
	
txt.close()
txt_again.close()