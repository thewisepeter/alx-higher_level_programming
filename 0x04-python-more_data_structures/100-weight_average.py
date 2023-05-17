#!/usr/bin/python3
def weight_average(my_list=[]):
    """function that returns the weighted
    average of all integers tuple (<score>, <weight>)
    returns 0 if list is empty"""
    if not my_list:
        return 0

    total_score = 0
    total_weight = 0

    for score, weight in my_list:
        total_score += score * weight
        total_weight += weight

    if total_weight == 0:
        return 0

    weighted_average = total_score / total_weight

    return weighted_average
