#!/usr/bin/python3
"""
Defines a function that returns
the list of available attributes
and methods of an object
"""


def lookup(obj):
    """
    Returns the list of available attributes
    and methods of obj

    Args:
        obj (object)
    """
    return (dir(obj))
