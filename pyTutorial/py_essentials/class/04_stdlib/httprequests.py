
import requests
from bs4 import BeautifulSoup


request = requests.get("http://jeremyosborne.com")
print request.status_code
text = request.text

parser = BeautifulSoup(text)
for a in parser.find_all("a"):
	if a.get("href"):
		print "Link found: " , a["href"]
	else: 
		print "No link found in this tag"