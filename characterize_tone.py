#!/usr/bin/python

# Create "good" and "bad" lists
# Initialize with synonyms from thesaurus
# Grab adjectives in a sentence 
	# if present, look at concordance
	# if not present need to analyze the emotional impact of certain words "waste", "treasure"

import load_config

def initialize(): 
	import urllib2, json

	
	good = ['good']
	bad = ['bad']
	key_info = load_config.read_keys('BigHugeLabs')
	key = key_info['key']

	for i in ['good', 'bad']:
		syn_endpoint = "http://words.bighugelabs.com/api/2/%s/%s/json" % (key, i)
		f = urllib2.urlopen(syn_endpoint) 
		syn_page = f.read()
		syn_json = json.loads(syn_page)	

		