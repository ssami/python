""" Our base Die class.
"""

from random import randint

class Die(object): 
	def __init__(self, faces=6):
		if type(faces) != int: 
			raise TypeError("Must pass an int value")
		elif faces < 1: 
			raise ValueError("Faces must be > 0")
		else: 
			self.faces = faces


	def roll(self): 
		return randint(1, self.faces)

	def __add__(self, other):
		if isinstance(other, Die):
			# if the other is a die, roll and add both values
			return self.roll() + other.roll()			
		elif type(other) == int:
			return self.roll() + other
		else: 
			raise TypeError("Other is not a die or an int!")
		
		