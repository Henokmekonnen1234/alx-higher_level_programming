#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key and type(key) is str and key in a_dictionary.keys():
        a_dictionary[key] = value
        return a_dictionary
    else:
        a_dictionary[key]  = value
        return a_dictionary
