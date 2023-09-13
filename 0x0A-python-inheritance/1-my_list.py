#!/usr/bin/python3
"""
Module 1-my_list.py

This module will be described below
"""


class MyList(list):
    """ This class inherit list from list class """

    def __init__(self):
        """initialation method

        Args:
            value (int): empty list
            count (int): numbers of elements in list
        """
        self.value = []

    def append(self, number):
        """ this method add numbers to the list

        Args:
            number (int): numbers passed to class
                          tobe added to the list
        """
        self.value.append(number)

    def print_sorted(self):
        """this method will sort the value list
            in accending order
        """
        print(sorted(list(self.value)))

    def __str__(self):
        """This will return list when the class called"""
        return f"{self.value}"
