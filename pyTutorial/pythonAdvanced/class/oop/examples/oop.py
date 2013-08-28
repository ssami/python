# Lab examples from tutorial 

## To do: 
# inherit from dictionary type
# pretty print values when people try to print
# Allow .dot access to keys


class SuperDict(dict):
	"""
	Inherits from dictionary type, pretty print values when people try to print
	Allow .dot access to keys
	"""
	def __init__(self): 
		# Python (2) super 
		dict.__init__(self)

	def __getattr__(self, name):
		# this is what is called when you try .access on an object
		return self[name]

	def __setattr__(self, name, value):
		self[name] = value

	def __str__(self):
		return ", ".join(self.values())

	def __add__(self, other):
		#return "\"%s\" and \"%s\"" % (self, other)
		if type(other) == dict: 
			for k, v in other.items(): 
				self[k] = v
		else: 
			raise TypeError("wrong error!")


if __name__ == "__main__":

	try: 
		d = SuperDict()
		d.test = "hello"		
		d["test"] = "hi there"
		print d["test"]				# item ... different from...  
		print d.test				# ... attribute
		d.test2 = "hey hey"
		d.test3 = "something else"
		print d
		f = {}
		f["first"] = "first"
		d + f
		print d
	except AttributeError as err: 
		print err
		


