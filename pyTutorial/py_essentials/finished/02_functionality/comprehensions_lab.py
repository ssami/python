""" 
    Lab
    ---
    
    Import our genpass function from our comprehensions module.
    Use it within a list comprehension to build a list of 10 passwords
    of length 20 using ascii letters, ascii digits, and ascii punctuation.
    When calling genpass, expand the list of arguments using the * notation.
    Enumerate and print out the passwords.
    
    Does our if __name__ == "__main__" code in our comprehensions module
    run? If not, why not? (This can be observed in the console, or rather
    by the lack of output in the console.)
"""

from comprehensions import genpass
import string

args = [20, string.ascii_letters+string.digits+string.punctuation]
passwords = [genpass(*args) for i in range(10)]

for i, password in enumerate(passwords):
    print i+1, password
