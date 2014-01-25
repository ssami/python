class Creature(object):
	"""
		TODO: 
		This is the class the monsters and angels inherit from 
		Every creature must have: a name, a description, an action and a response
	"""

	def __init__(self, letters):

		namelis = [letters[random.randint(0, x)] for x in range(1,len(letters))]
		
		self._name = namelis[0].capitalize() + ''.join(namelis[1:])


	def blah(self):
		print "blah"