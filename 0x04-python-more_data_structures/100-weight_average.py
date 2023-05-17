#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None:
        sum = 0
        regularity = 0
        for i in my_list:
            (weight, occurence) = i
            sum += (weight * occurence)
            regularity += occurence
        return (sum/regularity) if regularity > 0 else 0
    else:
        return (0)
