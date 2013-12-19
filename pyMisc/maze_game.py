from player import Player 
from room import Room
import random

if __name__ == "__main__":

	print "Hello! You're about to play the most awesome game ever"
	name = raw_input("What's your name? >>> ")
	if not name: 
		p = Player()
	else :
		p = Player(name)
	print "Welcome,", p.name
	if p.name == "Bozo":
		print "(See, this is why I asked you for your name... )"

	max_levels = 15
	level = 0
	
	while (p.health > 0 and level < max_levels) :
		goodness = random.randint(0, 10000) % 2
		r = Room(p, False, goodness)
		level += 1

	if p.health < 0:
		print "You died!"
	else : 
		print "This is all I can let you play"

