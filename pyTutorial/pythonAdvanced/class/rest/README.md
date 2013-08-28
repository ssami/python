What is a RESTful API?
======================
A 'RESTful API' is a remote API that follows the *REST* style of software architecture.



REST - Representational State Transfer
--------------------------------------
REpresentational State Transfer (REST) is a style of software architecture for distributed systems such as the World Wide Web. REST has emerged as a predominant Web service design model.

The term representational state transfer was introduced and defined in 2000 by Roy Fielding in his doctoral dissertation. Fielding is one of the principal authors of the Hypertext Transfer Protocol (HTTP) specification versions 1.0 and 1.1.

Conforming to the **REST constraints** is generally referred to as being "RESTful".

* [REST description](http://en.wikipedia.org/wiki/Representational_state_transfer)



JSON - Javascript Object Notation
---------------------------------
JSON, or *JavaScript Object Notation*, is a text-based open standard designed for human-readable data interchange. It is derived from the JavaScript scripting language for representing simple data structures and associative arrays, called objects. Despite its relationship to JavaScript, it is language-independent, with parsers available for many languages.

The JSON format was originally specified by Douglas Crockford, and is described in RFC 4627. The official Internet media type for JSON is `application/json`. The JSON filename extension is `.json`.

* [JSON homepage](http://json.org)
* [JSON description](http://en.wikipedia.org/wiki/JSON)



Requests Python Library
-----------------------
Requests is an HTTP library, written in Python, for human beings.

Requests takes all of the work out of Python HTTP/1.1, making your integration with web services seamless. There's no need to manually add query strings to your URLs, or to form-encode your POST data.

* [requests homepage](http://docs.python-requests.org/)



Using Requests to Generate a Github OAuth2 Token
------------------------------------------------
There are two ways to authenticate with the GitHub API: HTTP basic auth, and OAuth2. It is preferable to use OAuth2, so your script can run without user input, and without storing your password.

The OAauth2 token can be sent in the request header, or as a parameter.  We will send it as a header in later examples.



Requirements
------------
Before proceeding, we must install requests. Our code will likely work with any version of requests, but just in case we'll work with a specific version:

    pip install requests==0.12.1



POST Request
------------
First, we will prompt the user for username/password, and compose a POST request to the API.  The request format is documented in the [OAuth section](http://developer.github.com/v3/oauth/#create-a-new-authorization) of the Github API docs.

Try the `authtoken_0.py` example. (NOTE: PLEASE DON'T USE YOUR REAL PASSWORD IN THIS EXAMPLE!!!!)

    python authtoken_0.py

That's not good - our password is shown when we type it!



Password Privacy
----------------
We can protect the user's privacy while inputting their password with the `getpass` library.  While we're at it, we can prompt the user for an optional note to describe how this token will be used.

Let's give it a try:

    python authtoken_1.py 

Seems to have worked!  The response is a big JSON blob.



JSON Parsing
------------
We can parse the JSON response and provide just the token, in nice human-readable form, to the user.  

Explore the response data by setting a breakpoint and running our program in the debugger, or by pretty printing the output. The token lives in the creatively-named field `token`.  We will extract it and print it for the user.

Let's give it a try:

    python authtoken_2.py 

Bingo - it worked!



Error Handling
--------------
But what if we don't type the right username/password combo?

    python authtoken_2.py
    # Purposely use a bad user/password.

Debug the output. It looks like we have a `res.status_code` of 401.  Any HTTP response code 400 or above indicates an error.  It also looks like the server helpfully provides a `message` field with an error message.

We can look for response codes >= 400 and present the user a friendly error message:

    python authtoken_3.py 

Now we have a friendly, useful program.



Lab - Query github for user repositories
----------------------------------------
Using an API token that you generated in the previous example, work on `labs/list_repos.py` and see if you can work through the github API to get a list of repos for a user.

