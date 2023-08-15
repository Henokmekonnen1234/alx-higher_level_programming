#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        lisdiv = []
        for i in range(len(my_list)):
            if my_list[i] % 2 == 0:
                lisdiv.append(True)
            else:
                lisdiv.append(False)
    return lisdiv
