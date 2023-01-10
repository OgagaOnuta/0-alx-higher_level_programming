#!/usr/bin/python3
"""
Defines a function that checks
if an object is exactly an instance of
a specified class
"""


def is_same_class(obj, a_class):
    """
    Check if object is exactly an instance of a class

    Args:
        obj (object)
        a_class (class)

    Return:
        True if instance
        False if not instance
    """
    if (type(obj) == a_class):
        return (True)
    else:
        return (False)
