#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None or key is not None or value is not None:
        if key in a_dictionary:
            a_dictionary[key] = value
        else:
            a_dictionary[key] = value
        for keys in sorted(a_dictionary.keys()):
            print("{}: {}".format(keys, a_dictionary[keys]))
