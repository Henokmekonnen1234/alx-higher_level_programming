#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    return (map(lambda x: sum += x, set(my_list))) 
