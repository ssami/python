

class Room(object):
	"""
		The Room object is where the player encounters choices
		There will be a scenario, constructed from the Scene object
		If player chooses the monster scenario, player loses health 
		If player chooses angel scenario, player gains health
		In all cases, player will die or move to next room 
	"""



	def __init__(self, end=False, player):
		"""
			The end paramter denotes whether or not this room is the end. 
			If it's the end, the player just needs to pass whatever scenario is here and then exit successfully
			If not the end, the room will spawn other connected rooms and continue
		"""

		import random
		self.rooms = random.randint(1,5)	# get a random num of rooms for this room to connect to
		