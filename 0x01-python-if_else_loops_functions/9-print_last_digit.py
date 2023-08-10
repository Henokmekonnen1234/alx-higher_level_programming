#!/usr/bin/pytho3
def print_last_digit(number):
    if number == 0:
        print(0,  end="")
        return 0
    else:
        if number < 0:
            number *= -1
    print(number % 10, end="")
    return number % 10
