#!/usr/bin/python

import requests
import re
import bz2


c = requests.get('http://www.pythonchallenge.com/pc/def/integrity.html')

details = re.findall(r'un:\s+\'(.*)\'', c, re.I)
un = details[0]

details = re.findall(r'pw:\s+\'(.*)\'', c, re.I)
pw = details[0]

# print un and copy non-literal, non double backslash to un and pw

bz2.BZ2Decompress().decompress(un)
bz2.BZ2Decompress().decompress(pw)