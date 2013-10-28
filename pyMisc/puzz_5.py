#puzz_5.py

import pickle, requests

text = requests.get('http://www.pythonchallenge.com/pc/def/banner.p').content
data = pickle.loads(text)

def concatStuff(arr): 
	string = ''
	for i in arr: 
		if type(i) is list:
			concatStuff(i)
		else: 
			char, num = i
			while num > 0: 
				string += char
				num -= 1
	print string

concatStuff(data)