#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lDigit = int(repr(number)[-1])
if lDigit > 5:
    print("Last digit of", number, "is", lDigit, "and is greater than 5")
elif lDigit == 0:
    print("last digit of", number, "is", lDigit, "and is 0")
else:
    print("last digit of", number, "is", lDigit, end=' ')
    print("and is less than 6 and not 0")
