#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    usr = argv[1:]
    usr = [int(a) for a in usr]
    sum = 0
    for num in usr:
        sum += (num)
    print("{}".format(sum))
