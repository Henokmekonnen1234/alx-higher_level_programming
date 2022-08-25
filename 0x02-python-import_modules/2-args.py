#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    usr = argv[1:]
    length = len(usr)
    i = 1
    if length == 0:
        print("{} arguments.".format(length))
    elif length == 1:
        print("{} argument:".format(length))
        print("{}: {}".format(length, usr[0]))
    else:
        print("{} arguments:".format(length))
        for word in usr:
            print("{}: {}".format((i), word))
            i += 1
