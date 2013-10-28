#!/usr/bin/python
import requests, re


url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
maxtimes = 400 
append = "?nothing="
text = ""
next = 0 
alg = ""

# initial
text = requests.get(url).content
next = re.findall(r"href=.*nothing=([0-9]+)", text) 
url += append + next[0]

while maxtimes>0 :
	text = requests.get(url).content
	if (alg):
		next = []
		next.append(alg)
		alg = ""
	else: 
		next = re.findall(r"nothing is ([0-9]+)", text) 
	if (next):
		print next
		url = re.sub(r"[0-9]+", next[0], url)
		print url
		maxtimes = maxtimes - 1
		print maxtimes
		print "Next number: " + next[0]
	else: 
		print text
		alg = raw_input("What do you want to do now?")
		
