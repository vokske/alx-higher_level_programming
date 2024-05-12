#!/usr/bin/python3
"""Module contains class MyList."""


class MyList(list):
    """
    Class that inherits from list.

    Methods:
        print_sorted: Prints a sorted list.
    """
    def print_sorted(self):
            print(sorted(self))
