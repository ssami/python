class Monster(object):

	"""
		A monster is bad news for the player
		It depletes the player of health, but can be destroyed if player chooses the right choice
	"""

	def __init__(self):
		import random
		from bestiary import Bestiary

		lett = ['k', 'f', 'x', 'p', 'h', 'c']
		namelis = [lett[random.randint(0, x)] for x in range(1,len(lett))]
		
		self._name = namelis[1].capitalize() + ''.join(namelis[1:])
		self._description = Bestiary.getDescription()
		self._attack = Bestiary.getAttack()
		self._death = Bestiary.getDeath()
		self._pointsTaken = random.randint(-10, 0)

	@property
	def name(self):
		return self._name

	@property
	def description(self):
		return self._description

	@property
	def attack(self):
		return self._attack

	@property
	def pointsTaken(self):
		return self._pointsTaken

	@property
	def death(self):
		return self._death



if __name__ == "__main__":
	m = Monster()
	print "My monster name is", m.name
	print "I take away", m.pointsTaken, "points"

