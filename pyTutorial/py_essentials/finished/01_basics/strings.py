""" A varied but not exhaustive set of the string type and string 
    formatting examples.

    These examples only get into builtin and standard library
    string formatting in Python.
    
    With the inclusion of third party libraries you will have even more
    templating options.
"""


# There is a string module, although you probably won't use it much.
import string
# Perhaps the most useful thing on it are the lists of characters, example:
print string.letters
print string.digits



# Strings are immutable, iterable lists of characters.
# All of the strings are equivalent. Strings use backslashes to escape.
print "hello\nworld"
print 'hello\nworld'
print """hello
world"""
# This unicode string is equivalent visually...
print u'hello\u000Aworld'
# ...but not type wise.
print "Unicode equal to ascii?", type(u'hello\u000Aworld') == ('hello\nworld')
# Raw strings prevent escape sequences, good for regular expressions.
print r'hello\nworld'
# Sample string.
s = "i'm a lumberjack and i'm okay"
# Strings support index reference and slicing.
print "First letter:", s[0]
print "First word:", s[0:3]
print "Last word:", s[-4:]
print "Copy of the string:", s[:]
# Strings cannot be mutated.
try:
    s[0] = "o"
except TypeError as err:
    print "Can't change a string:", err
# Strings are objects and have methods.
print "Yelling:", s.upper()
print "Split on ' character:", s.split("'")
print s.replace("lumberjack", "programmer")
# The string calling join is the conjunction.
print 'programmer'.join(s.split("lumberjack"))
print "Lumberjack starts at index:", s.find('lumberjack')
# There is also strip() and lstrip().
print "No extra newlines\n\n\n\n\n\n".rstrip()



# printf style formatting.
print 'I would rather be in %s.' % 'Amsterdam'
# Multiple inputs wrapped in tuple.
print "We always write %s %s!" % ("hello", "world")
# Floating point formatting, here zero filled, 6 total characters,
# precision of 3.
print "A formatted float: %06.3f" % 10.5
# Can also use a dict, which allows mapping by name.
# dog left justified in a min field of 10 chars.
# num right justified in a minimum field of 24 chars, explicitly signed.
print "%(dog)-10s -> likes the number -> %(num)+24d" % {"dog": "fido", "num": 42}



# .format() style formatting.
# Implicit argument references.
print "Count to {} then to {}".format(10, 42)
# Explicit reference to the second argument (the first arg is not used).
print "Count to {1} then to {1}".format(10, 42)
# Note: must use explicit or implicit references, not both.
try:
    print "Count to {} then to {1}".format(10, 42)
except ValueError as err:
    print "Error:", err
# Data type formatting (using a multiline string).
print """int:   {0:d}
float: {0:f} 
hex:   {0:x}
oct:   {0:o} 
bin:   {0:b}""".format(42)
# References labeled argument.
"My quest is to find the golden {name}".format(name="nosehairs")
# Can reference object and type attributes by name.
class Orc(object):
    color = "green"
    pass    
o = Orc()
# Implicit reference to the first argument passed in.
print "The orc has {.color} skin".format(o)
# First indexed element of keyword argument 'players'.
"Good guys eaten by orcs: {goodguys[0]}".format(goodguys=[42])
# Left aligned in field of 30.
print '{:<30}'.format('left aligned')
# Right aligned in field of 30.
print '{:>30}'.format('right aligned')
# Centered in a field of 30.
print '{:^30}'.format('centered')
# Centered in a field of 30, white space filled with asterisks.
print '{:*^30}'.format('centered')  
# Forced stringification vs. forced pretty printing.
# (Note: objects may output the same thing. Strings have an obvious
# difference and are demonstrative of the potential difference.)
print "Stringified object: {!s}".format("hello world")
print "Pretty printed object: {!r}".format("hello world")



# $token string (UNIX shell like substitution).
# Class from the string module.
from string import Template
# Need to escape dollar signs. 
# Curly brackets for when delimiter not obvious.
t = Template('Owner of /$HOME/${user}dir owes $$$cost')
print t.substitute(HOME="Users", user="lucy", cost="100.00")
# dicts can also be passed in.
d = {"HOME":"Users", "cost":"OneMillion"}
# Error if we're missing some using normal substitue.
try:
    print t.substitute(d)
except KeyError as err:
    print "Substitute error on token:", err
# Following does not throw an error, leaves unreplacted tokens.
print t.safe_substitute(d)



# Regular Expressions are powerful.
# Unlike some languages, Regular Expressions are not builtins and need
# be imported before using.
import re
# Since regex does not allow for native patterns, we make patterns with
# strings. The following example demonstrates why raw strings are great.
test = "\\"
print "We have {} backslash.".format(len(test))
# Without raw strings, how many backslashes do we need? Lots.
# Because: backslashes are meaningful to the regex engine and the string.
print "Matches:", re.findall("\\\\", test)
print "Matches:", re.findall(r"\\", test)

# A test string.
test = """Kris Kringle, 
34th Miracle St., 
North Pole, 
3rd Rock,
kris@kringle.com"""
# Split on consecutive non-word characters.
print re.split(r"\W+", test)
# Replace consecutive numbers in a string.
print re.sub(r"\d+", "###", test)
# Replace only the first number.
print re.sub(r"\d+", "###", test, 1)
# Find consecutive word characters.
print re.findall(r"\w+", test)
# Escape special characters (make a pattern literal).
print re.escape("St.")
# Find cardinal directions, case-insensitive.
print re.findall(r"north|south|east|west", test, re.IGNORECASE) # or re.I
# Find the first word of a string.
print re.findall(r"^[^\W]+", test)
# Find the first word of each line of a multiline string.
print re.findall(r"^[^\W]+", test, re.MULTILINE) # or re.M
# Work with match objects with .match and .search.
# match must start matching on the first byte (even with multiline flag).
print re.match(r"^[\d]+", test, re.M)
# search will scan for the first match.
print re.search(r"^[\d]+", test, re.M)
# match objects make working with groups programmatically easier.
# Find a first and last name as named groups.
matches = re.search(r"^(?P<first>\w+) (?P<last>\w+)", test)
# Display our matches.
print matches.groups()
# Display the first match group.
print matches.group(1)
# Also display the first matched group.
print matches.group("first")
# Build a pattern.
pattern = "{}@{}\.com".format(matches.group("first"), 
                              matches.group("last"))
# Make it reusable and use it.
simple_email = re.compile(pattern, re.I) 
print simple_email.findall(test)
# Understand your regular expressions tomorrow morning.
print re.findall(r"""
                 [Kk]ris    # Sometimes he forgets to capitalize.
                 \          # whitespace must be explicit.
                 [Kk]ringle # Sometimes he forgets to capitalize.
                 """, test, re.VERBOSE) # or re.X
