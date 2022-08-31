#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        for keys in sorted(a_dictionary.keys()):
            print("{}: {}".format(keys, a_dictionary[keys]))
