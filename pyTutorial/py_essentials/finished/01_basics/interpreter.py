# The interpreter in python can be your best friend, both
# for experimentation and documentation about Python objects.
# All of the datatype examples should be run from a python
# interpreter.

# How to get the python version without entering the interpreter
# 
# python --version

# How to enter the interpreter from a terminal/console window
# python

# How to get help about an object or type (example, the int type)
# hit 'q' to get out of the help in most python interpreters.
help(int)

# Get a list of all module wide attributes, variables, methods, etc.
dir()

# Note that the output from the dir statement is in the python pretty printed
# format. The pretty print format will always show a list (square brackets)
# and all attribute names will be string elements in the list.

# Get a list of all attributes on an object or type
# (example, the int type)
dir(int)

# Import a module.
import math

# Math is now available as we can see.
dir()

# And we can get info about math.
dir(math)
help(math)

# Python has a lot of global builtins.
dir(__builtins__)

# Time to leave the commandline.
exit()
# or ctrl-d
