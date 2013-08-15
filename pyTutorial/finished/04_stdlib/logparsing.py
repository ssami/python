# Task: Parse the access log and count the unique ips accessing our server.



# For parsing.
import re
# For counting unique identities (there is more than one way to do this
# and I like Counter).
from collections import Counter
# In memory buffer for...
import io
# ...writing to a CSV file...
import csv
# ...and compressing our final output.
import gzip




# This pattern works with a small set of access logs that I gathered from
# my nginx server I run at home.
# This pattern will need to be adjusted based on any logfile modifications
# that you might use.
pattern = r'([\d\.]+|[:\d]+) - - \[(.*?)\] "(.*?)" (\d+|-) (\d+|-)'
regex = re.compile(pattern)

f = open("testdocs/access.log")
# Log entries as a list.
lines = f.readlines()
f.close()

# Form a list where things that don't match are strings and things
# that do match our regex are tuples.
accesses = map(lambda line: line if regex.match(line) is None else regex.match(line).groups(), lines)

# Find out if there are any malformed log entries.
bad = filter(lambda line: type(line) == str, accesses)
wellformed = filter(lambda line: type(line) == tuple, accesses)

print "Number of bad or unexpected log entries: %s" % len(bad)
print "Number of wellformed logs: %s" % len(wellformed)



# Our wellformed log entries can be counted.
print "Top 10 ips accessing our server."
top10 = Counter([el[0] for el in wellformed]).most_common(10)
for ip, count in top10:
    print ip, count



# Ideally we'd use io.StringIO(), but this will cause an error.
# The csv module does not like UTF8.
fbuffer = io.BytesIO()
csvwriter = csv.writer(fbuffer)
csvwriter.writerows(top10)
# Deflate (maximum compression) the CSV and write to a file.
gz = gzip.open('top10.csv.gz', 'wb')
gz.write(fbuffer.getvalue())
gz.close()
