#!/usr/bin/python3
"""Defines a file writing function."""


def write_file(filename="", text=""):
    """Write a string to UTF8 text file.
    Args:
        filename (str): The name of the file.
        text (str): The text to write.
    Returns:
        The number of characters.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
