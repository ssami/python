"""
A Python Package is synonymous to a folder that also contains a __init__.py
file (like this one).

The file can be empty or can have executable code and meta data in it.
"""

# There is no canonical way to mark version of a package.
__version_info__ = (0, 0, 1)
__version__ = '.'.join((str(info) for info in __version_info__))

# There is a lot of meta information you can add at your discretion.
__author__ = "me"

# What to import if someone import * our package.
__all__ = ["dice"]

