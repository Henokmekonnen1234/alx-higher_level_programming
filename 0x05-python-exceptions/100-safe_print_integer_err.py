#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as TE:
        sys.stderr.write("Exception: " + str(TE) + '\n' )
        return False
