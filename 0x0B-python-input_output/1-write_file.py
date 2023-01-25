#!/usr/bin/python3
"""Creates a function that writes a string to a text file
(UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """Write to a text file

    Args:
        filename : name of file
        text (string) : string to be written to file

    Return:
        Number of characters written

    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

    return (len(text))
