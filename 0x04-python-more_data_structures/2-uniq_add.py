#!/usr/bin/python3
def uniq_add(my_list=[]):
    """function that adds all unique integers
    in a list (only once for each integer)."""
    unique_list = list(set(my_list))
    sum = 0

    for i in range(len(unique_list)):
        sum += unique_list[i]
    return sum
