
class Bestiary(object):

	"""
		Stores all the descriptors for monsters: monster factory
	"""
	
	import random 

	"""
		Similar to Scenery, stores a list of descriptions and actions for monsters
	"""

	descriptions = [
		'a slavering beast with dripping jaws and terrible breath',
		'an insidious monster with more eyes than anyone could be comfortable with',
		'a slimy horror oozing with malevolence',
		'a scaly beast that towers over you',
		'a pepper pot-like creature that almost destroyed Gallifrey',
		'an android like creature that tried to enslave the human race'
	]


	attacks = [
		'rips you apart with its claws',
		'squeezes the life out of you with its tentacles',
		'squirts you with agonizing poison',
		'skewers you with antennae',
		'exterminates you',
		'upgrades you'
	]

	deaths = [
		'shrieks and dies',
		'gurgles and dies',
		'bellows and dies',
		'twitches and dies',
		'explodes in a shower of sparks'
	]

	@classmethod
	def getDescription(self):

		return self.descriptions[self.random.randint(0, len(self.descriptions)-1)]

	@classmethod
	def getAttack(self):

		return self.attacks[self.random.randint(0, len(self.attacks)-1)]

	@classmethod
	def getDeath(self):

		return self.deaths[self.random.randint(0, len(self.deaths)-1)]


if __name__ == "__main__":

	print "The monster that faces you is", Bestiary.getDescription()
	print "When you make a whimpering sound, it", Bestiary.getAttack()
	print "You recover your courage and attack back. It", Bestiary.getDeath()

