#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is not None and x is not None:
        try:
            x -= 1
            return (my_list[x])
        except IndexError:
            return (my_list[-1])
