#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    modulo = number % (-10)
else:
    modulo = number % 10

if modulo > 5:
    print("Last digit of {} is {} and is greater than 5"
          .format(number, modulo))
elif modulo == 0:
    print("Last digit of {} is {} and is 0"
          .format(number, modulo))
else:
    print("Last digit of {} is {} and is less than 6 and not 0"
          .format(number, modulo))
