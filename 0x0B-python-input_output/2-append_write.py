#!/usr/bin/python3
"""
Creates a function that appends a string
at the end of a text file (UTF8) and
returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file

    Args:
        filename : name of the file
        text (string) : string to be appended

    Return:
        Number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)

    return (len(text))
