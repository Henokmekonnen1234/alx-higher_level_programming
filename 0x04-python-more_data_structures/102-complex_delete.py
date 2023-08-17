#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value and a_dictionary:
        j = []
        for i, k in a_dictionary.items():
            if value == k:
                j.append(i)
        for a in j:
            del a_dictionary[a]
        return a_dictionary
    else:
        return a_dictionary
