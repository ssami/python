class People: 
	"""
		The class containing all the Player classmethods
	"""

	responses = {
		'bad' : ['refuse, churlishly', 'help, reluctantly'],
		'good' : ['help, graciously', 'are happy to assist'],
		'weird' : ['spontaneously break out into the Harlem shake', 'recite the Gettysburg Address from memory']
		
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
	def getResponses(self):
		resp = {}
		types = ['good', 'bad', 'weird']
		for t in types: 
			resp[t] = (self.getSingleResponse(t))


		return resp


if __name__ == "__main__":
	print People.getSingleResponse("good")
	print People.getSingleResponse("bad")
	print People.getSingleResponse("weird")
	print People.getSingleResponse("ugly")
	print People.getResponses()