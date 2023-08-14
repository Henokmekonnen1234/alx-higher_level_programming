#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        lisdiv = list(my_list)
        for i in range(len(my_list)):
            if my_list[i] % 2 == 0:
                lisdiv[i] = True
            else:
                lisdiv[i] = False
    return lisdiv
