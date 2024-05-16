#!/usr/bin/python3
"""Module contains class MyInt."""


class MyInt(int):
    """
    Inverts the operations of '==' and '!='

    Methods:
        __eq__()
        __ne__()
    """

    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
