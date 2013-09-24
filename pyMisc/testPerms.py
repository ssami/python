# Python idiom for listing differences between two lists: 

# orig = list(string) 
# sub = list("ab") 
# rem = [ i for i in orig if i not in sub ]

# but treats all characs are unique

# if not unique, 

# for i in sub: 
# 	orig.remove(i)






def attach(sub, string):
	partWords = []
	rem = []
	l = list(string)
	for i in sub: 
		l.remove(i)
	for i in l: 
		partWords.append(sub + i)

	for i in partWords: 
		if len(i) == len(string): 
			print i
		else: 
			attach(i, string)
