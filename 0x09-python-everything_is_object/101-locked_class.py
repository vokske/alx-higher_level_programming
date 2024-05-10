#!/usr/bin/python3
"""Module contains class LockedClass."""


class LockedClass:
    """
    Has no class or object attribute.
    Prevents user from dynamically creating new instance attributes.
    Only allows creation if attribute is called first_name.
    """
    __slots__ = ("first_name")
