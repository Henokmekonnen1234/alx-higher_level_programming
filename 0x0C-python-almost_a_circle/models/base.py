#!/usr/bin/python3
"""
Module base.py

This module will be described below
"""


class Base:
    """ Base class will be described

    Attributes:
        __nb_objects (int): private class instant
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """this method initializes the values 

        Args:
            id (int): we assign it to the values
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
