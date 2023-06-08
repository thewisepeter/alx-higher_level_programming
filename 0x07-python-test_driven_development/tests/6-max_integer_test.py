#!/usr/bin/python3
"""tests the max_integer function"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMax_Integer(unittest.TestCase):
    """unitests for max_integer"""
    def test_orderly(self):
        orderly = [1, 2, 3, 4]
        self.assertAlmostEqual(max_integer(orderly), 4)

    def test_empty(self):
        """empty list"""
        empty = []
        self.assertAlmostEqual(max_integer(empty), None)

    def test_one(self):
        """one member list"""
        one_member = [1]
        self.assertAlmostEqual(max_integer(one_member), 1)


if __name__ == '__main__':
    unittest.main()
