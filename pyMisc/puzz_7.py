#!/usr/bin/python

import png
from array import array
import re

imgdata = png.Reader('oxygen.png')
rgba = imgdata.asRGBA()
pixels = rgba[2]

rows = []
for i in pixels: 
	rows.append(i)


count = dict()
max = 0
row = 0
stchar = ''
for k, i in enumerate(rows): 
	start = i[0]
	if start in count: 
		count[start] += 1
		if count[start] > max: 
			max = count[start]
			stchar = str(unichr(start))
			row = k
	else: 
		count[start] = 1


chararr = rows[51].tostring().split('\xff')
clue = ''
sev = 7
for i in chararr: 
	ch = list(i)
	sev = sev - 1
	if (len(ch) > 0 and sev == 0): 
		clue += ch[0]
		sev = 7

print "Clue: " , clue 
match = re.search('\[(.*?)\]', clue)
nums = match.group(1)
numlist = nums.split(', ')
nextclue = ''
for i in numlist: 
	nextclue +=  unichr(int(i))

print "Next clue: ", nextclue

#print "Clue: " , ''.join(chararr)