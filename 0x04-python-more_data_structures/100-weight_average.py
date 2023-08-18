#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        sum = 0
        avr = 0
        for score in my_list:
            sum += score[0] * score[1]
            avr += score[1]
        return sum / avr
    else:
        return 0
