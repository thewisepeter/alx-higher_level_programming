#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """function that divides element by element 2 lists"""
    div_list = []

    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except (IndexError, ZeroDivisionError, TypeError):
            result = 0
        finally:
            div_list.append(result)
    return div_list
