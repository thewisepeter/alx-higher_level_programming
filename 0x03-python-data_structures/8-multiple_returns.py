#!/usr/bin/python3
def multiple_returns(sentence):
    """function that returns a tuple with the
    length of a string and its first character"""

    if len(sentence) == 0:
        tuple_return = len(sentence), None
    else:
        tuple_return = len(sentence), sentence[0]
    return tuple_return
