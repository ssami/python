""" Iterators in Python are interfaces.
"""

class HumanFriendlyCounter(object):
    """A class whose instances will be iterable.
    
    Will always iterate a count from 1-max, default 10.
    """
    def __iter__(self, max=10):
        """The initialization step for an iterator. This is implicitly
        called, for example, before a for loop is run.
        """
        self.current = 1
        self.max = max
        return self
    def next(self):
        """Each step of the iteration will respond to a call to next.
        When we are done, we must raise the StopIteration exception
        or we might continue forever.
        """
        if self.current <= self.max:
            n = self.current
            self.current += 1
            return n
        else:
            raise StopIteration()



# Human friendly count from 1 to 10.
c = HumanFriendlyCounter()
# Because c is iterable, we can use it directly in a for loop.
for number in c:
    print number


