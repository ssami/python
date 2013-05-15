import requests, re

#### Learning how to do regexes in Python 

def findAllLinks() : 
	"""Finding all the links in a document"""
	r = requests.get("http://www.google.com");
	p = re.compile('<a.*?>.*?</a>') 
	match = p.findall(r.content)
	for i in match: 
		print "here's this", i


