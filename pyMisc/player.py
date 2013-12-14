
class Player(object):
	"""
		The class that keeps track of the player instance
	"""


	def __init__(self, name="Bozo"):

		self._name = name
		self._health = 100

		print "Your name is", self._name , "and you start off with", self._health, "points"


	@property
	def name(self):
		return self._name

	@property
	def points(self):
		return self._health

	def changePoints(self, points):
		self._health += points




if __name__ == "__main__":
	p = Player()
	p.changePoints(-3)
	print p.points

