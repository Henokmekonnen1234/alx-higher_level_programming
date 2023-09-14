#!/usr/bin/python3
"""
Module 7-base_geometry.py

This module will be described below
"""


class BaseGeometry:
    """This class contain usefull methods"""

    def __init__(self):
        """empty intialization"""
        pass

    def area(self):
        """ unimplamented method

        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This method validates value variable

        Args:
            value (any): integer value
            name (str): string value

        Raises:
            TypeError: if value is not integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
