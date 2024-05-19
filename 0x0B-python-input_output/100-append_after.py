#!/usr/bin/python3
"""Module contains the function append_after."""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line\n
    containing a specific string.

    Args:
        filename: Name of the file.
        search_string: String to look for.
        new_string: String to be inserted.
    """
    with open(filename, "r") as f:
        lines = f.readlines()
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
