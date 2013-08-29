
# Allow easy importing from examples.
import sys
import os

this_dir = os.path.realpath(os.path.dirname(__file__))
sys.path.append(os.path.join(this_dir, "..", "examples"))        #sys.path is runtime python path - can add dir to import from
import fabfile_3

# ** is a labeled argument
# but we'll pass the *  because our tests are unlabeled

def execute(*args):
    try: 
        fabfile_3.hello(*args)      # passing these including the * means we're actually unpacking them
    except TypeError as err: 
         print "You haz error in hello: ", err
    try: 
        fabfile_3.arg_type(*args)   # if we passed them as (args) then we would pass a single argument - a list
    except TypeError as err: 
        print "You haz error in arg_type: ", err
    