"""Another utility for Python for high level system operations that you
want to manage in a Python-like way.

"""

import shutil
import os

backupdir = "backup"

# Make sure our directory exists.
os.makedirs(backupdir)

# Backup files in a directory.
print "Beginning backup procedure of our code..."
for f in os.listdir("."):
    if os.path.splitext(f)[1] == ".py":
        backdest = os.path.join(backupdir, f)
        print "copying {} to {}".format(f, backdest)
        # Keep some meta data, create directories between.
        shutil.copy2(f, backdest)

print "Backup completed. List of files in backup directory:"
for f in os.listdir(backupdir):
    print f

