#classes2.py

from classes import Employee 

class SuperNerd(Employee):
	def __init__(self, iq=150):
		Employee.__init__(self, "Poindexter")
		self.iq = iq

	def laugh(self): 
		return "%s laughs:", "hurk"*5

	def __str__(self): 
		return self.name + "has a %s IQ" % self.iq

	def __sub__(self, other):
		if type(other) == int: 
			self.iq -= other
		else: 
			raise TypeError("Sorry, can't operate with that paramter")

	def __add__(self, other):
		if type(other) == int: 
			self.iq += other
		else: 
			raise TypeError("Sorry, can't operate with that paramter")



if __name__ == "__main__":
	nerd = SuperNerd()
	nerd.iq -= 20
	print nerd
	print "Do we have a bowtie attribute?" , hasattr(nerd, "bowtie")
	nerd.bowtie = True 			#will not throw an error!
	print "Do we have a bowtie? ", nerd.bowtie
	print "Do we have a bowtie attribute?" , hasattr(nerd, "bowtie")
	print nerd
	nerd + 400
	print nerd

