#!/usr/bin/python3
def safe_print_list(my_list=[],x=0):
    counter = 0
    try:
        for i in my_list:
            counter += 1
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        print()
        return x
    except IndexError:
        #for i in range(counter):
            #print("{}".format(my_list[i]), end="")
        print()
        return counter
        

