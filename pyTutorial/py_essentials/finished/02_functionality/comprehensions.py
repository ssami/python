""" Python has to syntactic patterns for creating sequences:

    * a list comprehension creates a list sequence.
    * a generator creates an iterable function.
    
    In practice, list comprehensions are used when we need all elements of
    the list, and generators are used when we may not need all elements
    or we don't want all elements generated immediately.
"""

from random import choice
import string



def genpass(length=8, chars=string.letters+string.digits):
    """Generate a pseudo-random password.
    Also demonstrate the comprehension and generator idiom.
    """
    # The following:
#     pw = []
#     for i in range(length):
#         pw.append(choice(chars))
#     return ''.join(pw)

    # Can be rewritten as a list comprehension.
    #return ''.join([choice(chars) for i in range(length)])
    
    # Or a generator.
    return ''.join(choice(chars) for i in range(length))



if __name__ == "__main__":
    # The main block will often contain test code.
    print "Printing 6 random 8 character passwords."
    # Extra credit: make this modifiable via the command line.
    for i in range(6):
        print genpass()
