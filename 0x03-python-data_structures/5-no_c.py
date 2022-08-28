#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        my_string = list(my_string)
        for ind in range(len(my_string)):
            if ord('c') == ord(my_string[ind]) or ord('C') == ord(my_string[ind]): 
                my_string[ind] = ''
        my_string=''.join(my_string)
        return my_string
