#!/usr/bin/python3
import random
number = random.randint(-10, 10)
for x in range(number):
    if number < 0:
        print("{} is negative".format(number))
        break
    elif number > 0:
        print("{} is positive".format(number))
        break
    else:
        print("{} is zero".format(number))
