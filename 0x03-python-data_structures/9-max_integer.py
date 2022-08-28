#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    else:
        temp = 0
        for i in my_list:
            if temp < i:
                temp = i
        return temp
