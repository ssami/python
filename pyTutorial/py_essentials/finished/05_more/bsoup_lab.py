"""Lab:

* Grab all of the links from the LinkedIn Homepage.
* Make a list of links in a simple HTML file.
* Make sure the links work.

"""

import requests
from bs4 import BeautifulSoup
from io import StringIO
import re

domain = 'http://jeremyosborne.com/'

html = requests.get(domain).text
soup = BeautifulSoup(html)

out = """<!DOCTYPE html>
<html lang='en-US'>
    <head>
        <meta charset="UTF-8"/>
        <title>Some links</title>
    </head>
    <body>
        <h1>List of links from: {}</h1>
        <ul>
        {{}}
        </ul>
    </body>
</html>
""".format(domain)

links = StringIO()
template = "<li><a href='{0}{1[href]}'>{1.text}</a></li>"
for link in soup.find_all('a'):
    linkdomain = re.match(r"\/\/|http:\/\/|https:\/\/", link["href"])
    if linkdomain:
        # External link.
        linkdomain = ""
    else:
        # Relative link.
        linkdomain = domain
    links.write(unicode(template.format(linkdomain, link)))

with open("bsoup.html", "w") as f:
    f.write(out.format(links.getvalue()))

