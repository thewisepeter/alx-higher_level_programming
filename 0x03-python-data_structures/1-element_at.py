#!/usr/bin/python3
def element_at(my_list, idx):
    """function that retrieves an element from a list like in C"""
    length = len(my_list)
    if idx < 0:
        return None
    elif idx > length:
        return None
    else:
        return my_list.pop(idx)
