#!/usr/bin/python3
for n in range(0, 10):
    for i in range((n+1), 10):
        if (n is not 8) or (i is not 9):
            print("{}{}, ".format(n, i), end="")
        else:
            print("{}{}".format(n, i))
