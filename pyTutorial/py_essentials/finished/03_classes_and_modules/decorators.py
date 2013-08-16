""" Decorators are function wrappers in Python.

    They can be used on static functions and class functions/methods.

    Python does the function wrapping at run time.
"""



def increment_by_42(f):
    """A function meant to be a decorator.
    
    @param f The function we are going to wrap. This function is passed
    to us by the intepreter.
    
    @return A wrapped function.
    """
    def incrementor(*args):
        incremented = map(lambda n: n+42, args)
        return f(*incremented)
    
    return incrementor



# Apply our function wrapper.
@increment_by_42
def theanswer(*numbers):
    """Without wrapping, this function would just return the sequence.
    """
    return numbers



print "Results of our wrapped function:", theanswer(*range(5))
