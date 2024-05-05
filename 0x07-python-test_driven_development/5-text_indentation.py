#!/usr/bin/python3
"""Module contains the text_indentation function."""


def text_indentation(text):
    """
    Prints a text with two new lines after the characters '.', '?', and ':'.

    Args:
        text(str): random string

    Raises:
        TypeError: if text is not a string

    Returns: nothing
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    printed_text = ""
    lines = []
    for char in text:
        printed_text += char
        if char in (".", "?", ":"):
            lines.append(printed_text.strip())
            printed_text = ""
    if not lines:
        print(text.strip())
    for line in lines:
        print(line)
        print("\n" * 2)
