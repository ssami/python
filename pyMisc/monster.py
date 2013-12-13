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
			self.name = ''.join(namelis)

			self.description = Bestiary.getDescription()

