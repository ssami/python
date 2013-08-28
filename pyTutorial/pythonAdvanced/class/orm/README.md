Object Relational Mapping
=========================
Object Relational Mapping, or ORM, is a programming technique for mapping database objects into programming language friendly objects. Most programming languages have multiple tools for handling database datatypes to language datatypes. Understanding ORM is the point of this tutorial.

* see: [ORM definition](http://www.sqlalchemy.org/)



SQLAlchemy
----------
SQLAlchemy is an abstraction for SQL databases that provides ORM as well as other SQL tools. Before proceeding, make sure to do the following:

* [SQLAlchemy](http://www.sqlalchemy.org/)



Requirements
------------
Before proceeding, we'll need sqlalchemy:

    pip install sqlalchemy==0.8.1



Trying things out
-----------------
There is a simple example of using SQLAlchemy in the `examples/wrestler.py` module. Try things out and try changing things around to get an idea of the various aspects of how it works.



Lab
---
The lab consists of a simple SQL solution. Attempt to rip out the straight SQL and replace with an ORM provided by SQLAlchemy.
