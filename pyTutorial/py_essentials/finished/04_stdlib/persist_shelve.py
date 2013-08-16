# Shelve is a lot like pickle but is designed
# to be more database like.
# It's a simple key value database.
# Keys must be immutable python objects.
# Values can be anything that pickle can handle.

import shelve

# open with a general database name. There may be
# more than one actual file written, and the file may be
# given a file extension.
d = shelve.open("shelf")

# store data at key (overwrites old data if 
# using an existing key).
# Writing to the shelf should persist the data.
d["dog"] = "cat"

# Retrieve a copy of the data at the key, which
# is a bit different than how a normal dict
# works.
data = d["dog"]

# Check to make sure we got the data
print data

# delete data stored at key (raises KeyError
# if no such key)
del d["dog"]

# true if the key exists in the shelf. A good way to
# make sure 
flag = d.has_key(key)

# a list of all existing keys (slow!)
klist = d.keys() 

# close the connection (aka. file)
d.close()
