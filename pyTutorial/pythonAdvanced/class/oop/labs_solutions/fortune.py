""" Build a FortuneCookie class that contains a Fortune. FortuneCookies
can be opened to produce Fortunes.

# Build the Fortunes from a class method on Fortune.
>>> Fortune.sayingsFromString("Your favorite number is 42\\nYour favorite color is red, no blue!")
>>> Fortune.sayings
['Your favorite number is 42', 'Your favorite color is red, no blue!']

# FortuneCookie class has two states: opened and not opened.
>>> cookie = FortuneCookie()
>>> try:
...     cookie.read()
... except ValueError:
...     print "Sorry, can't read an unopened cookie."
Sorry, can't read an unopened cookie.

# Once opened, the same fortune is available for all time to read.
>>> cookie.open()
>>> cookie.read()
'Your favorite number is 42'
>>> cookie.read()
'Your favorite number is 42'
    
>>> cookie2 = FortuneCookie()
>>> cookie2.open()
>>> cookie2.read()
'Your favorite color is red, no blue!'

# What happens when we run out of fortunes.
>>> cookie3 = FortuneCookie()
>>> cookie3.open()
>>> cookie3.read()
'Generic fortune for you.'

# The FortuneCookie ancestry.
>>> isinstance(cookie3, Fortune)
True
>>> isinstance(cookie3, FortuneCookie)
True
"""


class Fortune(object):
    sayings = None
    def __init__(self):
        if Fortune.sayings:
            self.saying = Fortune.sayings.pop(0)
        else:
            self.saying = "Generic fortune for you."
    def read(self):
        return self.saying
    @classmethod
    def sayingsFromString(cls, sayings):
        cls.sayings = sayings.split("\n")

class FortuneCookie(Fortune):
    def __init__(self):
        self.fortune = Fortune()
        self.opened = False
    def open(self):
        if not self.opened:
            self.opened = True
    def read(self):
        if not self.opened:
            raise ValueError("Can't read an unopened cookie.")
        else:
            return self.fortune.read()
        

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
