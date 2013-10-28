#!/usr/bin/python


import re
import string

code = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

listcode = list(code)
for i, c in enumerate(listcode): 
	if c in string.lowercase:
		ind = string.lowercase.index(c)
		if ind+2 > len(string.lowercase)-1:
			newind = ((ind+2) % (len(string.lowercase)-1)) - 1 
			print "NEw index: ", newind, " corresp char: ", string.lowercase[newind]

		else: 
			newind = ind+2
		newchar = string.lowercase[newind]
		listcode[i] = newchar

print ''.join(listcode)


################


shiftchars = list(string.lowercase)[-2:] + list(string.lowercase)[:-2]
map = string.maketrans(''.join(shiftchars), string.lowercase)
string.translate(code, map)
