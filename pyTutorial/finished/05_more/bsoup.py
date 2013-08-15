# The Python Package Index (PyPI) is to Python
# what CPAN is to Perl
# and npm is to node.js
# and PECL/PEAR is to PHP.

# The canonical installer for third party tools was easy_install
# but is now pip
#
#     http://www.pip-installer.org

# We assume virtualenv has been used.

# From here, let's download beautifulsoup and requests if we don't have
# it:
#
#     pip install beautifulsoup4
#     pip install requests

# The documentation for beautifulsoup is easy to find by searching for it.
# beautifulsoup is an HTML parser, much like ElementTree, except friendly
# to plain old XML. Now that we've installed it, we can use it.
# Assuming that testdocs/example.xml exists.

import requests
from bs4 import BeautifulSoup

html = requests.get('http://jeremyosborne.com/').text

soup = BeautifulSoup(html)

print "\nCleaned up content:\n%s" % soup.prettify() 
print "\nContent of the <title> tag:\n%s" % soup.title
print "\nContent of the <body> tag:\n%s" % soup.body

print "\nLinks from this page and where they are going:"
anchors = soup.find_all('a')
for anchor in anchors:
    print "%40s href to -> %s" % (anchor.text, anchor["href"])

print "\nAny imported scripts?"
scripts = soup.find_all('script')
for script in scripts:
    try:
        print "%40s href to -> %s" % (script.text, script["src"])
    except KeyError:
        print "Script without src, must be an inline script."
        print "Contents of inline script:"
        print script.text

print "\nIs this document in a certain encoding?"
try:
    print "\tYes, it is: %s" % soup.find(lambda el: el.has_key('charset'))["charset"]
except:
    print "\tNo language declared for this document."

# And if you want to uninstall it when you're done:
#    pip uninstall beautifulsoup4
#    pip uninstall requests
