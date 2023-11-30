#!/usr/bin/python3
"""
Module 6-peak.py
"""


def find_peak(list_of_integers):
    """this will ge peak in a list of unsorted integers."""
    if list_of_integers:
        list_of_integers.sort(reverse=True)
        return list_of_integers[0]
