#!/usr/bin/python

def validate_phone(number):
	import re

	# validate only numbers
	if re.findall('[a-z'], number):
		print "Invalid number; has letters!"
		return -1

	# validate correct length
	nums = re.findall('[0-9]', number)
	if len(nums) != 7: 
		print "Not a valid number length in the United States!"
		return -1

	