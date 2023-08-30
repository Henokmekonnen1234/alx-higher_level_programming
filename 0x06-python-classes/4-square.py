#!/usr/bin/python3
""" Module 4-square.py

This Module defies the Square class
"""


class Square:
    """this class define about the square class"""

    def __init__(self, size=0):
        """intialaize the size instance

        Args:
            size (int, optional): length of the sizes
        """
        self.__size = size

    @property
    def size(self):
        """Getter method

        Return:
            int: the value of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method

        Args:
            value (int, optional): int value to  set size

        Raise:
            TypeError: if size is not integer
            ValueError: if size < 0
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the are of square

        Return:
            int: the square of the sides
        """
        return self.__size ** 2
