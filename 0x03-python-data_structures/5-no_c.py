#!/usr/bin/python3
def n0_c(my_string):
    if my_string is not None:
        for ind in range(len(my_string)):
            if ord('c') == ord(my_string[ind]) and ord('C') == ord(my_string[ind]):
                my_string[ind] = ''
        return my_string
