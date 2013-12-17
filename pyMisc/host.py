class Host(object):

	"""
		Stores all the descriptors for Angels: angel factory
	"""


	import random

	descriptions = [
		'a luminous being of light, holding cookies',
		'a sparkling creature, with the voice of Chris Martin',
		'a divine beauty, bearing every Terry Pratchett novel'
	]

	disappears = [
		'vanishes with a tinkling laugh',
		'winks and disappears',
		'smiles beatifically and fades into nothingness'
	]

	requests = [
		'asks for help moving furniture',
		'asks for really good Peruvian coffee',
		'asks for good restaurant recommendations',
	]


	@classmethod
	def getDescription(self):

		return self.descriptions[self.random.randint(0, len(self.descriptions)-1)]

	@classmethod
	def getDisappearance(self):

		return self.disappears[self.random.randint(0, len(self.disappears)-1)]

	@classmethod
	def getRequest(self):

		return self.requests[self.random.randint(0, len(self.requests)-1)]