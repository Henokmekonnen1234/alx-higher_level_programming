#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary.keys() and type(key) is str:
        a_dictionary[key] = value
        return a_dictionary
    else:
        a_dictionary[key] = value
        return a_dictionary
