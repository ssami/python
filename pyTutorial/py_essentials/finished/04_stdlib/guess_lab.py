# Number guessing game.
# * Ask the user their name.
# * If the user has played before, welcome them back and display their
#   wins and losses.
# * If the user is new, welcome them to the game.
# * Let the user know they will need to guess a number between 1 and
#   20 in 5 tries.
# * If the user guesses the number, it is a win.
# * If the user does not guess the number, it is a loss.
# * Tell the user, if they do not guess the number, whether their guess
#   is high or low.
# * If the user loses, tell them the number.
# * Somehow persist name, win, loss stats between games
# * Allow the user to quit at anytime by typing "quit"
# * Allow the user to replay the game when they've officially
#   won or lost.
#

from random import randint
import sys
import re
import shelve

guessesAllowed = 1
guessesTaken = 0

stats = shelve.open("guessstats")

print "Hello! Would you like to play a game?"
answer = raw_input()

if answer:
    if answer.upper()[0] != "Y":
        print "Okay, you can not play."
        sys.exit(1)
else:
    sys.exit(1)

print "Okay, what is your name."
# NOTE: Ran into odd errors with the unicode output from raw_input
# and the shelf code. Convert to string.
name = str(raw_input())

if stats.has_key(name):
    print "Welcome back", name
    print "You have", stats[name]["wins"], "wins and", stats[name]["losses"], "losses."
else:
    print "Hello new player", name
    # Initialize stats for player
    stats[name] = {"wins": 0, "losses": 0}


print "Your job is to guess a number between 1 and 20."

number = randint(1, 20)

while guessesAllowed > guessesTaken:
    print "Take a guess."
    try:
        guess = raw_input()

        if re.match("q", guess):
            print "Your game is over"
            stats.close()
            sys.exit()

        guess = int(guess)
        
        guessesTaken += 1

        if guess == number:
            print "You haz won the internetz."
            stat = stats[name]
            stat["wins"] += 1
            stats[name] = stat
            break
        elif guess > number:
            print "You have guessed to high."
        elif guess < number:
            print "You have guessed to low."
    except ValueError:
        print "Please guess a number."

if guess != number:
    print "The number was", str(number)
    stat = stats[name]
    stat["losses"] += 1
    stats[name] = stat
    

stats.close()
