#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if search is None or replace is None or my_list is None:
        return my_list
    else:
        return list(map(lambda x: replace if x == search else x, my_list))
