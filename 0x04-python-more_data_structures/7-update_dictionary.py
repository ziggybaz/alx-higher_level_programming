#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None:
        dic_two = {key: value}
        a_dictionary.update(dic_two)
        return(a_dictionary)
    else:
        return None
