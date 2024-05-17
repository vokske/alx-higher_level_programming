#!/usr/bin/python3
"""Module contains the write_file function."""


def write_file(filename="", text=""):
    with open(f"{filename}", mode="w", encoding="utf-8") as testFile:
        return testFile.write(f"{text}", end="")
