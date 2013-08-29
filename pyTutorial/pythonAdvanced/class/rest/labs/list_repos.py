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

API_TOKEN = 'f9306e18d54e75cd25fa6890905c8920ff2d20db'
VALID_TYPES = ['all', 'owner', 'public', 'private', 'member']
REPOS_API = 'https://api.github.com/user/repos'
ISSUES_API= 'https://api.github.com/repos/' 

import requests
import argparse
from urlparse import urljoin
import json

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
    
    print "Looking for repos of type: ", args.type
    payload = {'type' : args.type[0]}
    res = requests.get(
            REPOS_API,
            data = json.dumps(payload),
            headers = headers
    )
    
    ######
    
    #
    #    The problem is that the Github API for some reason doesn't filter by type
    #    So we have to get the entire response back and then filter by private or not
    
    #####
       
    #print res.json()[1].keys()
    
#     for repo in res.json():
#         print "%s : %s" % (repo["name"], repo["description"])
    
#     if args.type == "all":
#         for repo in res.json(): 
#             print "%s : %s" % (repo["name"], repo["description"])
#     else:

    def filter_function(x):
        if args.type[0] == "public":
            return x["private"] == False
        if args.type[0] == "private":
            return x["private"] == True
        else: 
            return True

    for repo in filter(filter_function, res.json()):
        print "%s : %s" % (repo["name"], repo["description"])
    
    
if __name__ == '__main__':
    main()
