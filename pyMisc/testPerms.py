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
