# puzz_10.py

#!/usr/bin/python

# this is useful: http://en.wikipedia.org/wiki/Look-and-say_sequence

start = '1'
nums = []
nums.append(start)

k = 0
while k < len(nums) and len(nums) < 31: 
	n = nums[k]
	# print "Now doing", n
	digits = list(n)
	count = 0
	curr = digits[0]
	prev_ind = 0
	new_num = ''
	list_of_dig = []


	i = 0 
	while i < len(digits):
		if digits[i] != curr: 
			sl = digits[prev_ind:i]
			list_of_dig.append(sl)
			prev_ind = i
			curr = digits[i]
		i += 1

	# print "Prev_ind:", prev_ind, " i:", i
	if prev_ind < i: 
		list_of_dig.append(digits[prev_ind:i])

	if i == 0:
		list_of_dig.append(digits)

	# print list_of_dig
	for p in list_of_dig: 
		new_num += str(len(p)) + str(p[0])
		
	# print "New num:", new_num
	# print "Length of num:", len(new_num)
	nums.append(new_num)

	k += 1


print "Length of 30th element:", len(nums[-1])
