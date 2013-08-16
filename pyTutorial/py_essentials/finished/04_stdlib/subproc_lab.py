# Run the ls -lh command and count the number of lines of 
# output from stdout.
# Display the number of lines from ls -lh.
# Bonus points: How many directories are in the output?

from subprocess import *
import os
import re

stdout = check_output(["ls", "-lh"])

print "ls output %s lines." % len(stdout.split("\n"))

# Extra credit.
# This allows for cross OS friendly lineseparators.
print "There are %s dirs." % len(re.findall(r"(?<="+os.linesep+")d", stdout))
