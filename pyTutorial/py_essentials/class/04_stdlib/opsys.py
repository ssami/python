"""
Python offers multiple ways of working with the operating system.
The os module provides basic tools for working with the os. os does 
not guarantee that all methods work across all platforms.
"""

import os


print "Our OS indicator:", os.name
# What environment variables are set.
print "env:", os.environ
# Value of a specific environment variable.
print "PATH:", os.path.expandvars("$PATH")

print "pwd:", os.getcwd()
# Get directory containing this file, even if script executed elsewhere.
d = os.path.realpath(os.path.dirname(__file__))
print "pwd of script:", d

somedir = os.path.join(d, 'somedir')
os.mkdir(somedir)
print "list of dirs after making one", os.listdir(d)
# like rm -r for dirs.
os.removedirs(somedir)




import re

def findfiles(path, ext=".pyc"):
    """ Returns a list of all files of an extension in a path.

    @param path {str} Initial path to the directory we
    want to crawl.
    @param [ext=".pyc"] {str} what file extensions to look for. This is
    a literal match and must contain the dot.
    """
    tree = os.walk(path)
    results = []
    regex = re.compile(re.escape(ext)+"$", re.I)
    for d in tree:
        # Each element of a walker represents a directory and its contents.
        # Diagnostic, if you wish.
        #print(d)
        if d[2]:
            # Are there files in this directory?
            for f in d[2]:
                if regex.findall(f):
                    relpath = os.path.join(d[0], f)
                    results.append(os.path.realpath(relpath))

    return results

# Note: It's possible that the user does not have .pyc files. Try another
# extension like .py.
for path in findfiles("../"):
    print "File found:", path
    # If the user is feeling brave, they can use:
    if raw_input("Do you wish to delete this file? ").lower() == "y":
        print "Removing file:", path
        os.remove(path)
