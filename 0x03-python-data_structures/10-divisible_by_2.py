#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if my_list:
        data = []
        for i in my_list:
            if i % 2 is 0:
                data.append(True)
            else:
                data.append(False)
        return data
