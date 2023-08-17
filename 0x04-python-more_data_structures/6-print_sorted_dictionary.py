#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        sorted_value = sorted(a_dictionary.keys())
        for i in sorted_value:
            print("{}:  {}".format(i, a_dictionary[i]))
