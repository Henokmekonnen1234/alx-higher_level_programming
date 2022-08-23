#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    temp = (number * -1) % 10
else:
    temp = number % 10

if temp == 0:
    print(f"Last digit of {number} is {temp} and is 0")
elif temp < 6 and temp != 0:
    print(f"Last digit of {number} is {temp} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {temp} and is greater than 5")
