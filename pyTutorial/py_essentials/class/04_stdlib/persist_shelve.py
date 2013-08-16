
import shelve

name = str(raw_input("What's your name? "))
quest = str(raw_input("What's your quest? "))
color = str(raw_input("What is your favorite color? "))

questor = (name, quest, color)
shelf = shelve.open("questors.slv")

if name in shelf: 
	print "You're already here!"
	print shelf[name]
else: 
	print "We're preserving your quest forever!"
	shelf[name] = questor

shelf.close()