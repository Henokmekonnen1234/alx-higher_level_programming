#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temp = str(number)
temp = temp[-1:]
if int(temp) == 0:
    print(f"Last digit of {number} is {int(temp)} and is 0")
elif int(temp) < 6 and int(temp) != 0:
    print(f"Last digit of {number} is {int(temp)} and is less than 6 and not 0")
elif int(temp) > 5:
    print(f"Last digit of {number} is {int(temp)} and is greater than 5")
