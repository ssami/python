# puzz_9.py
#!/usr/bin/python

import requests
from requests.auth import HTTPBasicAuth
import re
import png


url = "http://www.pythonchallenge.com/pc/return/good.html"
uname = "huge"
pwd = "file"
resp = requests.get(url, auth=(uname, pwd))
if resp.status_code == 200:
	print "Successfully authenticated!"
	content = resp.text
	matched = re.search('first\:\n(.*)second\:\n(.*).*-->', content, re.M|re.S)
	first = matched.group(1)
	second = matched.group(2)

	images = []
	images.append(first)
	images.append(second)

	for ig in images:
		import turtle

		ig = ig.replace('\n', '')
		nums = ig.split(',')
		x_arr = []
		y_arr = []
		for ind, num in enumerate(nums):
			# print "index:", ind, " number:", num 
			if (ind % 2 == 1):
				y_arr.append(int(num))
				# print "stored in y arr"
			else:
				x_arr.append(int(num))
				# print "stored in x arr"


		img_arr = []
		img_arr.append(x_arr)
		img_arr.append(y_arr)
		print img_arr

		#png.from_array(img_arr, 'LA').save('test.png')

		for a, b in zip(x_arr, y_arr):
			turtle.goto(a, b)

		raw_input()
		turtle.clear()

else: 
	print "Cannot authenticate! Error code:",resp.status_code 



# You'll go to http://www.pythonchallenge.com/pc/return/cow.html
# and then be taken to http://www.pythonchallenge.com/pc/return/bull.html after you figure out that male bovine animals are bulls