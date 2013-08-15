import random

# Get the list of secret words.
# The file should have one word per line.
# OR
# Could retrieve words from (need a more specific URL available at
# this site, this site is just a web page of lists.)
# http://dictionary-thesaurus.com/wordlists.html
# OR MORE FUN
# Grab words from the TaleofTwoCities.txt.
words = open("../testdocs/words.txt", "r").read().split()
# What is our word?
secret = random.choice(words)
# Start off with vowels guessed, but this can be changed to make things
# harder (or easier).
guessed_letters = 'aeiou'
# Total number of incorrect guesses allowed.
# If you change this, should change the picture of the hangman.
mistakes_allowed = 5
# Current number of mistakes.
mistakes = 0

def show_hangman(mistakes):
    """Shows the hangman according to the current number of mistakes.
    
    Returns a formatted string ready for display.
    """
    # Should be one piece for each letter allowed.
    hangman_parts = []
    if mistakes > 0: hangman_parts.append('   O   ')
    if mistakes > 1: hangman_parts.append(' \_|_/ ')
    if mistakes > 2: hangman_parts.append('   |   ')
    if mistakes > 3: hangman_parts.append('  / \  ')
    if mistakes > 4: hangman_parts.append(' d   b ')
    return '\n'.join(hangman_parts)


print ""
print 'time to play hangman'.title()
print ""

# Runs each and every turn.
while mistakes < mistakes_allowed:
    print "The secret word so far:"
    # Count of unguessed letters.
    missing_letters = 0
    for letter in secret:
        if letter in guessed_letters:
            # If the letter has already been guessed, show it.
            print letter,
        else:
            # Blank space for each unguessed letter.
            print '_',
            missing_letters += 1
    # Blank line after the letters.
    print ""
        
    if missing_letters == 0:
        # You win! Resolve winning and losing outside of this loop.
        break

    print ""
    print "You have guessed the following letters:"
    print guessed_letters
    print ""
    
    guess = raw_input('guess a letter: ')
    if not guess or len(guess) > 1:
        print "Please guess one letter at a time."
    elif guess in guessed_letters:
        print "Please guess a letter you have not yet guessed."
        continue
    else:
        guessed_letters += guess
        if guess not in secret:
            mistakes += 1
            print 'Nope.'
            print '%s mistakes made, %s more mistake%s allowed.' % (
                        # How many mistakes have we made?
                        mistakes, 
                        # How many more mistakes?
                        mistakes_allowed - mistakes,
                        # Pluralize the word correctly if we need to.
                        "s" if (mistakes_allowed-mistakes > 1) else "")
            print show_hangman(mistakes)

# Determine if the player won or lost.
if missing_letters == 0:
    print "You win!"
else:
    print "Sorry, you did not win."
    print "The word was:", secret
