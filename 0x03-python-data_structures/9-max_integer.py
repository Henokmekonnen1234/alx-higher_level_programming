#!/usr/bin/python3
def max_integer(my_list=[]):
    temp = 0
    if my_list is not None:
        for i in my_list:
            if temp < i:
                temp = i
                print(my_list)
        print(my_list)
        return temp
