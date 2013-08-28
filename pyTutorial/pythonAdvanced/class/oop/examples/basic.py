class Employee(object):
    """New style classes always inherit from an object or type. If we want
    a base class with no frills, inherit from object.
    
    As classes are "called" just like functions are called when an instance
    is created (there is no special constructor keyword like new), a style
    is to TitleCase a class name.
    """
    
    title = "Peon"
    """Class attributes are fallback attributes shared by all instances
    unless overwritten."""
    
    def __init__(self, name):
        """The init method is the constructor method and is called when an
        instance is created.
        
        All methods, init or otherwise, are implicitly passed the self
        reference argument as the first argument, however we as developers
        must explicitly reference this self in our class method signatures.
        When using class methods, except in certain situations we actually
        pass in n-1 arguments. For example, this constructor takes 1
        argument when called regularly.
        """
        
        # Python objects are dynamic by default. This is the standard way
        # of initializing an instance attribute.
        self.name = name

    def talk(self, message="How can I help you?"):
        """Allow our employee to talk.
        """
        return "{} says: {}".format(self, message)
    
    def __str__(self):
        """Default methods can be overridden. Here, we pretty print 
        ourselves when we attempt to string substitute an instance.
        
        There are many methods that can be overridden.
        """
        return "{} ({})".format(self.name, self.title)
    
    def __eq__(self, other):
        """Operators can be overridden. Here we override the equality
        operator in a very simplistic and naive way.
        
        @param other The right hand operand.
        """
        # We can compare an instance to a class like so.
        if isinstance(other, Employee):
            return True
        return False



class Boss(Employee):
    """Boss inherits from Employee.
    """
    
    title = "Boss"
    """We override anything we want to change."""
    
    def __init__(self, name):
        """Within a subclass, we can explicitly call inherited methods.
        When we do, we must explicitly plass the self reference, too.
        """
        Employee.__init__(self, name)
        
        # Stylistically, underscores denote private properties.
        self._bloodpressure = 100
    
    def talk(self, message=None):
        """Override the talk message.
        """
        return Employee.talk(self, "Like a boss.")
    
    @property
    def bloodpressure(self):
        """A computed property, declared with a decorator.
        Access to stress is as an attribute, not as a function.
        """
        self._bloodpressure += 10
        return self._bloodpressure
    
    @classmethod
    def default_title(cls):
        """Class methods are not propagated to instances, they are part
        of the class object.
        
        Much like instance methods receive the instance implicitly when
        called on instances, class methods receive a reference to the
        class object.

        They are the static method (Java) types of Python
        """
        return "The default title of %s is %s" % (cls.__name__, cls.title)

if __name__ == "__main__":
    # There is no new keyword in Python. Call the class to instantiate.
    grunt = Employee("Idle")
    print "Employee name:", grunt.name
    print "Employee:", grunt
    print grunt.talk()
    print grunt.talk("I want a raise.")

    boss = Boss("Cleese")
    print "Boss Name:", boss.name
    print "Boss:", boss
    print boss.talk()
    print boss.talk("I want a raise.")
    
    print "Are Cleese and Idle equal?", boss == grunt

    print "Boss stress level:", boss.bloodpressure
    print "Boss stress level:", boss.bloodpressure
    print "Hidden props aren't actually hidden:", boss._bloodpressure

    print "Calling class method Boss.title():", Boss.default_title()
