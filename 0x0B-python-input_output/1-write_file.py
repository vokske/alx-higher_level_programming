#!/usr/bin/python3
"""Module contains the write_file function."""


def write_file(filename="", text=""):
    """
    Writes to a file or creates it if it doesn't exist.

    Args:
        filename: Name of the file.
        text: String to be written onto the file.
    """
    with open(f"{filename}", mode="w", encoding="utf-8") as testFile:
        return testFile.write(f"{text}", end="")
