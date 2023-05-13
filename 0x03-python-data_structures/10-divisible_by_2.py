#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """function that finds all multiples of 2 in a list"""
    new_list = []
    for num in my_list:
        new_list.append(num % 2 == 0)
    return new_list
