#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list.copy()
    elif idx > (len(my_list) - 1):
        return my_list.copy()
    else:
        lists = my_list.copy()
        lists[idx] = element
        return lists
