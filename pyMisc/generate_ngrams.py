## Generates n-grams based on document input

import sys 

# Generates ngrams based on the 
def gen_ngrams (n, words) : 
	if n < 1 : 
		print "N-grams must be order 1 or higher!" 
		sys.exit(1)
	else : 
		lines = words.split("\n")
		#print "No. of lines: %d" % len(lines)
		ngrams =[]
		for l in lines :
			words = l.split()
			for i in range(0, len(words)) : 
				#print words[i:i+n]
				if i+n <= len(words) : 
					phrase = ' '.join(words[i:i+n])
					ngrams.append(phrase)
			
	return ngrams
				 


# Generates all ngrams from unigrams to n-grams specified in parameters
#def gen_upto_ngrams () : 
	
grams = []
grams = gen_ngrams(2, "hi there\nhere's a kettle of fish!\no")
print grams