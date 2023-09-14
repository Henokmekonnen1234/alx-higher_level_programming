#!/usr/bin/python3
"""
Module 8-rectangle.py

This module described below
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This class inherited from BaseGeometry class"""

    def __init__(self, width, height):
        """ this method will initiate the args when it's called

        Args:
            width (any): the first argument
            height (any): the second argument
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
