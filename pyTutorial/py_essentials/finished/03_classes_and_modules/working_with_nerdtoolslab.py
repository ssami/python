# Adding a package folder to the PYTHONPATH at runtime.
import sys
import os

dpath = os.path.join(os.path.dirname(__file__), "nerdtoolslab")
sys.path.append(os.path.realpath(dpath))

# And now we can import our nerdtoolslab.
from nerdtoolslab import *
print "I rolled a d20 and all I got was:", dice.D20().roll()
print "I rolled a d6 and all I got was:", dice.D6().roll()
