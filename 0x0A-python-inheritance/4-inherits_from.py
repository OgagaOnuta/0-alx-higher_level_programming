#!/usr/bin/python3
"""
Defines a function that checks if an 
object is a subclass of a specified class
"""


def inherits_from(obj, a_class):
    """
    Check if object is a subclass of a class

    Args:
        obj (object)
        a_class (class)

    Return:
        True if instance
        False if not instance
    """
    if (issubclass(type(obj), a_class)):
        return (True)
    else:
        return (False)
