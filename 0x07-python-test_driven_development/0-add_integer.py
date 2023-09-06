#!/usr/bin/python3
"""
Module 0-add_integer.py

This module supplies one function add_integer for  adding integer
"""


def add_integer(a, b=98):
    """ this fuction addes two int or float numbers
    Raise:
        TypeError: a must be an integer or  b must be an integer"""
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
