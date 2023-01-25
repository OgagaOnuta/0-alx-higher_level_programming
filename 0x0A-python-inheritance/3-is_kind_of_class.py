#!/usr/bin/python3
"""Defines a function that checks if an object is an 
instance of a specified class or it's child class
"""


def is_kind_of_class(obj, a_class):
    """Check if object is an instance of a class or it's child class

    Args:
        obj (object)
        a_class (class)

    Return:
        True if instance
        False if not instance

    """
    if (isinstance(obj, a_class)):
        return (True)
    else:
        return (False)
