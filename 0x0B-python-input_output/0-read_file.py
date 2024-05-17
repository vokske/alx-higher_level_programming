#!/usr/bin/python3
"""Module contains the read_file function."""


def read_file(filename=""):
    """
    Reads a text file and prints it to stdout.

    Args:
        filename: Name of the file.
    """
    with open(f"{filename}", encoding="utf-8") as readFile:
        print(readFile.read())
