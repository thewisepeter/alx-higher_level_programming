#!/usr/bin/python3
def remove_char_at(str, n):
    """function that creates a copy of the string
    removing the character at the position n"""
    i = 0
    str_cpy = ""
    for char in str:
        if i == n:
            i += 1
            continue
        else:
            str_cpy += char
            i += 1
    return str_cpy
