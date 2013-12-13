
class SceneDescriptors(object):

	descriptors = {
		"good":[
			'The mist clears away to reveal a luxurious lounge room',
			'Everything in this room is sleek, as though it were in homage to Steve Jobs',
			'Unicorns and ponies abound in this atmosphere',
		], 
		"bad":[
			'There is a serious sense of foreboding in this room',
			'The walls are slick with slime and there is an overpowering stench',
			'This room is unhealthily red',
		]}

	def getScene(self, good=False):
		"""
			Good: boolean parameter which gives you a "good" or "bad" scenario
		"""
		import random

		descList = []
		if good: 
			descList = self.descriptors['good']
		else : 
			descList = self.descriptors['bad']

		r = random.randint(0,len(descList)-1)
		return descList[r]



if __name__ == "__main__":
	sd = SceneDescriptors()
	print "Good scenario:	", sd.getScene(True)
	print "Bad scenario:	", sd.getScene(False)