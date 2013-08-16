


import urllib
import urllib2
from urlparse import urlparse



# Simple request generates a file like object.
data = urllib.urlencode({"cats": 42, "chickens": 2, "dogs": None})
# Sending data makes request a POST instead of a get.
response = urllib2.urlopen("http://jeremyosborne.com/class/formtest.php",
                           data)

# See the url we worked with
print "Response from:", response.geturl()
print "Response from hostname:", urlparse(response.geturl()).hostname
print "Status code:", response.getcode()

# Dictionary of headers and interate over them.
for name, value in response.info().items():
    print "{}: {}".format(name, value)

with open("response.html", "w") as f:
    # Response is streamlike.
    f.write(response.read())

