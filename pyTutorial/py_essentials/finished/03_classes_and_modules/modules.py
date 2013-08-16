""" A module is synonymous to a file in Python.

    Using a simple module, we can see a few things about how modules work
    that might already be apparent.

    * Run the module from the commandline and note the number of print
    outputs.
    * Open the python interpreter and import this module. Note the
    number of print outputs you see.
    * Import the module again. Note the number of print outputs.
    * Change the value of modules.x. Print the value of modules.x.
    Is it still 100? Why not?
    * Import modules again and print out the value of modules.x.
    Why is the value the way it is? What do you think other modules will
    see if they also import modules and reference modules.x (within the
    same application runtime)?
"""

# This will be data accessible to those who import the module.
x = 100

print "Visible when run or imported."

if __name__ == "__main__":
    print "Only visible when run."
