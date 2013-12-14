from creature import Creature

class Angel(object):

	"""
		The Angels bestow points on the players of the game if they do something right
	"""

	def __init__(self):

		import random	
		from host import Host

		lett = ['s', 'w', 'a', 'e', 'l', 'v', 'm', 'i']
		namelis = [lett[random.randint(0, x)] for x in range(1,len(lett))]
		
		self._name = namelis[0].capitalize() + ''.join(namelis[1:])
		self._description = Host.getDescription()
		self._disappear = Host.getDisappearance()
		self._pointsGiven = random.randint(1, 10)


	@property
	def name(self):
		return self._name

	@property
	def description(self):
		return self._description

	@property
	def pointsGiven(self):
		return self._pointsTaken

	@property
	def disappear(self):
		return self._disappear


if __name__ == "__main__":
	a = Angel()
	print "My angel name is", a.name
	a.blah()


