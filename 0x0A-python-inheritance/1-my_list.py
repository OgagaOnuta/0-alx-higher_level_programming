#!/usr/bin/python3
"""
Defines a class that inherits the list object
"""


class MyList(list):
    """ Inherits from the list object """
    def __init__(self):
        list.__init__(self)

    def print_sorted(self):
        """
        Prints a sorted list
        """
        print(sorted(self))
