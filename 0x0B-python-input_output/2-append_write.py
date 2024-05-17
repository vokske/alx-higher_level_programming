#!/usr/bin/python3
"""Module contains the append_write function."""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file.

    Args:
        filename: Name of the file to which text will be appended.
        text: The text to be appended.
    """
    with open(f"{filename}", mode="a", encoding="utf-8") as testFile:
        return testFile.write(f"{text}")
