#!/usr/bin/python3
"""
Module 10-square.py

This module described below
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """this class iherited from Rectangle class"""

    def __init__(self, size):
        """this method initializes when the class called

        Args:
            size (any): legth of the sides
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """this method claculates sides

        Returns:
            int: area of squares
        """
        return self.__size ** 2
    
    def __str__(self):
        """string representation of the class"""
        return f"[{self.__class__.__mro__[1].__name__}] {self.__size}/{self.__size}"
