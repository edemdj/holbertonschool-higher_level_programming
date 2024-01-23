#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDigit = int(repr(number)[-1])
if number > 5:
    print( "Last digit of", number, "is", lastDigit, "and is greater than 5")
elif number == 0:
    print("last digit of", number, "is", lastDigit, "and is 0")
else:
    print("last digit of", number, "is", lastDigit,"and is less than 6 and not 0")
