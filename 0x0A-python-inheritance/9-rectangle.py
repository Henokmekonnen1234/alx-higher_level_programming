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

    def area(self):
        """calculates the area of Reactagle

        Returns:
            int: the area of rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """when the class called this will be called"""
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
