# splitting words into things that make sense 

def build_bigram_source(source_text=None, filter=50):
	"""
		Builds bigrams out of a source text. Usually news
		source_text is a string, or is blank. If a string, will be tokenized, etc
		filter is an integer that lets you filter out 
	"""

	import nltk
	from nltk.collocations import BigramAssocMeasures	
	bigram_measures = nltk.collocations.BigramAssocMeasures()

	print "Building your very own bigram table... \n"
	if not source_text: 
		finder = nltk.collocations.BigramCollocationFinder.from_words(nltk.corpus.abc.words())
	else: 
		from nltk.tokenize import word_tokenize, sent_tokenize
		tokens = [word for sent in sent_tokenize(source_text) for word in word_tokenize(sent)]
		finder = nltk.collocations.BigramCollocationFinder.from_words(tokens)

	finder.apply_freq_filter(filter)

	return finder


def split_query(clean_query=None, bigram_dict=None):
	"""
		Splits a query in the most "English sensible way" 
		Uses a previously defined bigram source dictionary
	"""
	import nltk
	from nltk.collocations import *

	if not clean_query: 
		print "This isn't a valid query!"
		return None
	if not bigram_dict: 
		print "You didn't provide a valid bigram dictionary!"
		return None

	tokens = clean_query.split(' ')
	window = 2 # default is bigrams
	for ind, tok in enumerate(tokens):
		if ind+1 < len(tokens):
			bigram_measures = nltk.collocations.BigramAssocMeasures()
			bscore = bigram_dict.score_ngram(bigram_measures.pmi, tokens[ind], tokens[ind+1])
			if bscore: 
				print "Bigram score for: '",tokens[ind],"' and '",tokens[ind+1],"' is",bscore
			
	