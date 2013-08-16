# We need:
#
#     pip install requests
#
# 

import requests
import os
import re

# Get the initial batch of image URLs.
r = requests.get('http://jeremyosborne.com/class/pictures.php')
image_urls = r.json()["urls"]

# Content types that we'll allow.
pattern = r"^image/jpg|^image/jpeg"

nextfile = 0
for url in image_urls:
    print "Retrieving data from:\n\t%s" % url
    # Get the file extension from the URL.
    ext = os.path.splitext(url.rstrip("/"))[1]
    r = requests.get(url)

    ct = r.headers["content-type"]
    if re.match(pattern, ct):
        nextfile += 1
        out_path = "out%s%s" % (nextfile, ext)
        print "\twriting data to: %s" % out_path
        # Images are binary files...
        f = open(out_path, "wb")
        # ...and we can get the response as binary content.
        f.write(r.content)
        f.close()
    else:
        print "\tUnexpected Content-Type of %s" % ct

