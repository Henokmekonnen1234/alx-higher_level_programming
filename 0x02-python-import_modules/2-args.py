#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argvs = sys.argv
    if len(argvs) == 1:
        print("{:d} arguments.".format(0))
    elif len(argvs) == 2:
        print("{:d} argument:".format(1))
        print("{:d}: {}".format(1, argvs[1]))
    else:
        print("{:d} arguments:".format(len(argvs) - 1))
        for i in range(1, len(argvs)):
            print("{:d}: {}".format(i, argvs[i]))
