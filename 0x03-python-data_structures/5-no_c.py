#!/usr/bin/python3
def no_c(my_string):
    strs = list(my_string)
    i = 0
    while i < len(strs):
        if strs[i] == 'c' or strs[i] == 'C':
            strs.pop(i)
        i += 1
    my_string = " ".join(strs)
    return my_string
