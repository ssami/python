class People: 
	"""
		The class containing all the Player classmethods
	"""

	responses = {
		'bad' : ['refuse, churlishly', 'help, reluctantly'],
		'good' : ['help, graciously', 'are happy to assist'],
		'weird' : ['spontaneously break out into the Harlem shake', 'recite the Gettysburg Address from memory']
		
	}

	defenses = {
		'bad' : ['scream and try to run away', 'tremble and then faint', 'gurgle and die'], 
		'good' : ['destroy it with a fireball', 'vanquish it with the power of your mind', 'bore it to death'],
		'weird' : ['twerk', 'impersonate Chuck Norris', 'sing the Habenera from Carmen']
	}


	import random

	@classmethod
	def getSingleResponse(self, kind='good'):

		try: 
			li = self.responses[kind]
			return li[self.random.randint(0, len(li)-1)]
		except: 
			print "That type is not in the list of responses! Select from 'good', 'bad', and 'weird'"

	@classmethod
	def getSingleDefence(self, kind='good'):

		try: 
			li = self.defenses[kind]
			return li[self.random.randint(0, len(li)-1)]
		except: 
			print "That type is not in the list of defences! Select from 'good', 'bad', and 'weird'"



	@classmethod
	def getResponses(self):
		resp = {}
		types = ['good', 'bad', 'weird']
		for t in types: 
			resp[t] = (self.getSingleResponse(t))


		return resp

	@classmethod
	def getDefenses(self):
		defs = {}
		types = ['good', 'bad', 'weird']
		for t in types: 
			defs[t] = (self.getSingleDefence(t))


		return defs


if __name__ == "__main__":
	print People.getSingleResponse("good")
	print People.getSingleResponse("bad")
	print People.getSingleResponse("weird")
	print People.getSingleResponse("ugly")
	print People.getResponses()