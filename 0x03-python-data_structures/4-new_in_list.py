#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    shallow_list = my_list.copy()
    if idx >= 0 and idx < len(my_list):
        shallow_list[idx] = element
    return shallow_list
