'''
Lab - List Repositories

Write a script that queries the Github API for repositories 
belonging to the authenticated user.

Github defines several types of repository that can be listed:

* all
* owner
* public
* private
* member

Our application should query for `all` by default, but allow the user to
specify a different type.

For each repo, print out its name, its description, and the number
of open issues.

Use [argparse](http://docs.python.org/dev/library/argparse.html) to
define commandline arguments.
'''

API_TOKEN = 'YOUR_TOKEN_GOES_HERE'
VALID_TYPES = ['all', 'owner', 'public', 'private', 'member']

import requests
import argparse

def main():
    parser = argparse.ArgumentParser(description='List Github repositories.')
    parser.add_argument('-t', '--type', 
        nargs = 1,
        dest = 'type',
        default = 'all',
        metavar = 'TYPE',
        choices = VALID_TYPES,
        help = 'What type of repos to list',
        )
    args = parser.parse_args() # You can access the 'type' argument as args.type
    #
    # Use the authentication token we generated in the previous example
    #
    headers = {
        'Authorization': 'token %s' % API_TOKEN
        }
    #
    # Now, build a REST request, and parse the server's response...
    #
    
    
if __name__ == '__main__':
    main()
