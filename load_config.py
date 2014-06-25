#!/usr/bin/python

import sys

def read_keys(app, config_file="keys.config"): 
	import json
	if app is None: 
		print >> sys.stderr, "Application name must be non-null, e.g. Twitter"
		sys.exit(-1)

	f = open(config_file, 'r')
	key_info = json.load(f)
	return key_info[app]

if __name__ == "__main__": 
	read_keys('Twitter')
