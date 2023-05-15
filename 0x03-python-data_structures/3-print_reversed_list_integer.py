#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    reverse_copy = my_list.reverse()
    if reverse_copy != None:
        for i in reverse_copy:
            print("{:d}".format(i))
