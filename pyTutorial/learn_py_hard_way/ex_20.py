from sys import argv
import math

script, input_file = argv

def print_all(f) : 
	print f.read()

def rewind(f) : 
	f.seek(0)
	
def print_a_line(line_count, f): 
	print line_count, f.readline()

def compound_interest(sum, percentage, years) : 
	total_money = math.pow((percentage + 1), years) * sum
	return total_money

current_file = open(input_file) 

print "First let's print the whole file:\b"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file) 

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)


print "I'm leaving %d in the bank." % 100
print "The total amt of money I get after leaving %d in the bank for 5 years at 10 percent interest is %f" % (100, compound_interest(100, 0.1, 5))