#!/usr/bin/python3
"""
Module 2-is_same_class

This is the function of this module and will be described below
"""


def is_same_class(obj, a_class):
    """this methos will compare instances

    Args:
        obj (optional): the first argument
        a_class (optional): the second argument

    Returns:
        Boolean: True if the obj is an instance of a_class or else False
    """
    return isinstance(obj.__class__, a_class)
