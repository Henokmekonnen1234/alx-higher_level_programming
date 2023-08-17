#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        i = 0
        for j, k in a_dictionary.items():
            if i < k:
                i = k
                name = j
        return name
    else:
        return None
