#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    else:
        max_value = 0
        for i in my_list:
            if max_value < i:
                max_value = i
        return max_value
