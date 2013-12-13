

class Bestiary(object):
	
	import random 

	"""
		Similar to Scenery, stores a list of descriptions and actions for monsters
	"""

	descriptions = [
		'a slavering beast with dripping jaws and terrible breath',
		'an insidious monster with more eyes than anyone could be comfortable with',
		'a slimy horror oozing with malevolence',
		'a scaly beast that towers over you',
	]


	attacks = [
		'rips you apart with its claws',
		'squeezes the life out of you with its tentacles',
		'squirts you with agonizing poison',
		'skewers you with antennae'
	]

	deaths = [
		'shrieks and dies',
		'gurgles and dies',
		'bellows and dies',
		'twitches and dies'
	]

	def getDescription(self):

		return self.descriptions[self.random.randint(0, len(self.descriptions)-1)]

	def getAttacks(self):

		return self.attacks[self.random.randint(0, len(self.attacks)-1)]

	def getDeaths(self):

		return self.deaths[self.random.randint(0, len(self.deaths)-1)]



if __name__ == "__main__":

	b = Bestiary()
	print "The monster that faces you is", b.getDescription()
	print "When you make a whimpering sound, it", b.getAttacks()
	print "You recover your courage and attack back. It", b.getDeaths()

