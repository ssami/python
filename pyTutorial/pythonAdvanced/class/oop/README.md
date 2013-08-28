Object-oriented programming
===========================
[Object-oriented programming](http://en.wikipedia.org/wiki/Object_oriented_programming), or OOP, is a way of programming that approaches problems, challenges, data, and even processes from an noun-centric point of view. If I was building a digital farm, I might have Animal objects that have data fields representing traits, and functions, or methods, that represent what the animal can do. If I was running a bulletin board, I might have Users, Forums, Messages, and other objects representing the data and activities allowed on my board.

Unlike a language like Java, Python expresses itself as an OOP language along with other paradigms. Mastering OOP in Python is a part of the path along which one travels to master Python as a whole.



Tools available to the OOP programmer in Python
-----------------------------------------------
OOP is more of a style of programming that is dependent on the language one is in. We want to take a look at some of the not-immediately-obvious features of OOP prgramming in Python.



Basics
------
Run `examples/basic.py` and walk through the code to review some of the way OOP is expressed in Python.



Metaclasses and Interfaces
--------------------------
One of the biggest reasons to use OOP in Python is mainly due to the amount of power it provides the developer. Run `examples/abstract_and_interfaces.py` and walk through the code.

* see: [The Python Abstract Base Class](http://docs.python.org/2/library/abc.html)
* see: [Metaclasses, what are they? (a long but good answer on stackoverflow)](http://stackoverflow.com/a/6581949)
* see: [Python Data Model, class interfaces and overrides](http://docs.python.org/2/reference/datamodel.html)



Multiple Inheritance
--------------------
Python exhibits what is called multiple inheritance, where one object can inherit from more than one immediate parent.

Run `examples/mi.py` and walk through the code.

Multiple inheritance is difficult to do right, but can be useful with patience and in certain situations. Open up the code in `examples/mi.py` and comment out the update functions. Why does the code still work?

* see: [Python Method Resolution Order](http://www.python.org/download/releases/2.3/mro/)



Labs
----
Go through the labs to exercise some of the not-always used features of OOP in Python, as well as some of the regularly used features.
