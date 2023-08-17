#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary:
        newDict = {}
        for i, k in a_dictionary.items():
            newDict[i] = k * 2
        return newDict
