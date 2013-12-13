#!/usr/bin/python

import os, zipfile, re, shutil, urllib, zlib

if not os.path.exists('puzz6'): 
	resp = urllib.urlretrieve("http://www.pythonchallenge.com/pc/def/channel.zip")
	tdir = resp[0]
	shutil.copy(tdir, "channel.zip")
	z = zipfile.ZipFile("channel.zip")
	z.extractall("puzz6")

tfile = "puzz6/90052.txt"
comms = []
c = "y"

if c is "y": 
	z = zipfile.ZipFile("channel.zip")
	# continue parsing through unzipped files, starting from 90052.txt
	while c is "y":
		f = open(tfile)
		clue = f.read()
		print clue
		num = re.findall('[0-9]+', clue)
		if not num: 
			break
		tfile = "puzz6/" + num[0] + ".txt"
		deets = z.getinfo(num[0] + ".txt")
		comms.append(deets.comment)
		print tfile


print ''.join(comms)





