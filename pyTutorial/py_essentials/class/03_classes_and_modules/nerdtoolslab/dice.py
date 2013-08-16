""" Die subclasses.
"""

from die import Die


class D6(Die):
	def __init__(self):
		Die.__init__(self, 6)


class D20(Die):
	def __init__(self):
		Die.__init__(self, 20)

	
if __name__ == "__main__": 
	d6 = D6()
	d20 = D20()
	print d6 + d20
	print d6 == d20
	