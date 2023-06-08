#!/usr/bin/python3
"""tests the max_integer function"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMax_Integer(unittest.TestCase):
    """unitests for max_integer"""
    def test_orderly(self):
        """test an ordered list"""
        orderly = [1, 2, 3, 4]
        self.assertAlmostEqual(max_integer(orderly), 4)

    def test_disorderly(self):
        """Test an ordered list of integers."""
        disorderly = [3, 2, 1, 4]
        self.assertEqual(max_integer(disordered), 4)

    def test_floats(self):
        """test floats"""
        floats = [1.3, 2.5, 3.6, 4.7]
        self.assertAlmostEqual(max_integer(floats), 4.7)

    def test_repeated_number(self):
        repeated_number = [2, 2, 1, 2]
        self.assertAlmostEqual(max_integer(repeated_number), 2)

    def test_floats_ints(self):
        """test floats and ints"""
        floats_ints = [1.4, 2, 3.5, 4]
        self.assertAlmostEqual(max_integer(orderly), 4)

    def test_string(self):
        """test a string"""
        string = "Peter"
        self.assertAlmostEqual(max_integer(string), r)

    def test_empty_string(self):
        """test an empty string"""
        empty_string = ""
        self.assertAlmostEqual(max_integer(empty_string), None)

    def test_list_string(self):
        """test a list with a single string"""
        list_string = ["Peter"]
        self.assertAlmostEqual(max_integer(list_string), 'Peter')

    def test_list_of_strings(self):
        """test a list with strings"""
        list_of_strings = ["Peter", "is", "great"]
        self.assertAlmostEqual(max_integer(list_of_strings), 'is')

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
