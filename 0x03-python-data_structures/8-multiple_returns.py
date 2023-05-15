#!/usr/bin/python3

def multiple_returns(sentence):
    str_length = len(sentence)
    char = sentence[0] if str_length > 0 else None

    return (str_length, char)
