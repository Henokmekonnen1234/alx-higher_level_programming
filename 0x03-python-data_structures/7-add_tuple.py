#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        if tuple_a and tuple_a == None:
            tuple_a[0] = 0
            tuple_a[1] = 0
        elif tuple_a[1] == None:
            tuple_a[1] = 0
    elif tuple_b and len(tuple_b) < 2:
        if tuple_b == None:
            tuple_b[0] = 0
            tuple_b[1] = 0
        elif tuple_b[1] == None:
            tuple_b[1] = 0 
    else:
        sum = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
        return sum
