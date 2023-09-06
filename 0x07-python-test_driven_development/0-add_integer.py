#!/usr/bin/python3
"""
Module 0-add_integer.py

This module supplies one function add_integer for  adding integer
"""


def add_integer(a, b=98):
    """ this fuction addes two int or float numbers
    Args:
        a (int, float): the first int or float number
        b (int, float): the second int or float number

    Raise:
        TypeError: if a is not an integer or float number
        TypeError: if b is not an integer or float number

    Return:
        int: the sum of a and b will be returned
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    a = int(a) if type(a) is float else a
    b = int(b) if type(b) is float else b
    return a + b
