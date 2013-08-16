""" Python has the concept of truthy and falsey, as in some things can
	pass a truth check, and some things will fail a truth check besides
	True and False.
"""

# Truth tests.
falsehoods = [None, False, 0, 0L, 0.0, 0j, "", (), [], {}]

# An excuse to use a while loop, one of the control structures we have
# yet to see.
while len(falsehoods):
	truthcheck = falsehoods.pop()
	if not truthcheck:
		# If we ever need a single element tuple.
		# repr is a prettyprint function.
		print "%s is not truthy." % (repr(truthcheck),)

