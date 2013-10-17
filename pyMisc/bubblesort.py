#!/usr/bin/python



orig_arr = [2, 56, 2, 7, 9, 4, 2, 6, 3, 5, 6, 9, 4]

swap = True

while (swap):
	swap = False 
	for ind, num in enumerate(orig_arr):
		if ((ind+1 < len(orig_arr)) and (num > orig_arr[ind+1])): 
			temp = num
			orig_arr[ind] = orig_arr[ind+1]
			orig_arr[ind+1] = temp
			swap = True
	if not swap: 
		break



for i in orig_arr: 
	print i 
