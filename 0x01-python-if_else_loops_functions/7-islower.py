#!/usr/bin/python3
def islower(i):
    """checks for lowercase character"""
    if ord(i) in range(97, 123):
        return True
    else:
        return False
