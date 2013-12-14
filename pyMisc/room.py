

class Room(object):
	"""
		The Room object is where the player encounters choices
		There will be a scenario, constructed from the Scene object
		If player chooses the monster scenario, player loses health 
		If player chooses angel scenario, player gains health
		In all cases, player will die or move to next room 
	"""

	def __init__(self, player, end=False, good=False):
		"""
			The end paramter denotes whether or not this room is the end. 
			If it's the end, the player just needs to pass whatever scenario is here and then exit successfully
			If not the end, the room will spawn other connected rooms and continue
			If "good" is false, this room will have bad things in it
		"""

		import random
		from scenery import SceneDescriptors
		from monster import Monster
		from angel import Angel

		self._rooms = []
		_roomNum = random.randint(1,3)							# get a random num of rooms for this room to connect to
		for i in _roomNum: 
			goodness = random.randint(0, 1000) % 2				# flip a coin to generate goodness
			# end? need to figure out how to end
			if (player.health > 0):
				self._rooms.append(Room(player, False, goodness))
			else: 
				print "HEALTH ZERO. YOU DIE. GO AWAY."
		self._description = SceneDescriptors.getScene(good)
		if good: 
			self._creature = Angel()
		else: 
			self._creature = Monster()




