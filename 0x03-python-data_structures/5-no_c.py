#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        lists = list(my_string)
        for ind in range(len(lists)):
            if ord('c') == ord(lists[ind]) or ord('C') == ord(lists[ind]):
                lists[ind] = ''
        my_string = ''.join(lists)
        return my_string
