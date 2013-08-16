import datetime
from pprint import pprint

#pprint (vars(datetime.date))

def find_age (born_year) : 
	current_year = datetime.date.today().year
	age = current_year - born_year
	return age
	
print "When were you born?"
year = int(raw_input())
age = find_age(year)
print "So you're %d years old!" % age

#print "Here is a question: " 
#print "What is your name?" 
#name = raw_input('>>')
#print "Hi, %s!" % name 
#
#print "What is your age?"
#age = raw_input(">>") 
#print "So you're %r years old eh?" % age

find_age(234)
