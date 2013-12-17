

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
		from host import Host
		from people import People
		from player import Player

		self._rooms = []
		_roomNum = random.randint(1,3)							# get a random num of rooms for this room to connect to
		for i in range(_roomNum): 
			goodness = random.randint(0, 1000) % 2				# flip a coin to generate goodness
			# end? need to figure out how to end
			if player.health > 0 and not end:
				self._rooms.append(Room(player, True, goodness))
		self._description = SceneDescriptors.getScene(good)
		if good: 
			self._creature = Angel()
			print "The angel", self._creature.name, "appears before you. It is", self._creature.description, ". It", Host.getRequest()
			print "Your choices are: "
			resp = People.getResponses()
			for key, val in enumerate(resp):
				print key, ".", resp[val]

			print "Now, what will you do? Select a number"
			
			choice = ''
			invalid = True
			while invalid:
				choice = raw_input("-->")
				if int(choice) > len(resp)-1:
					print "That number is invalid! Try again"
				elif int(choice) < 0:
					print "That number isn't even a positive number! Try again"
				else:
					print "You selected", choice
					invalid = False

			choiceType = resp.keys()[int(choice)]
			choiceText = resp[choiceType]		# always prints only one from each good, bad, wierd list anyway
			typeMap = {
				'good': True, 
				'bad': False, 
				'weird': False
			}

			if typeMap[choiceType]:
				print "The angel bestows upon you", self._creature.pointsGiven, "health and", self._creature.disappears
				player.changeHealth(self._creature.pointsGiven)

			else: 
				print "The angel is annoyed. It smites you and takes away", self._creature.pointsGiven, "health"
				player.changeHealth(-1 * self._creature.pointsGiven)
				
			print "You now have", player.health, "health left"



		else: 
			self._creature = Monster()



if __name__ == "__main__":
	from player import Player

	p = Player()
	r = Room(p, True, True)