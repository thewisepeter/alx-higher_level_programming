#!/usr/bin/python3
#test module for the class Base
import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    #Test Base Class

    def test_initial_id(self):
        obj1 = Base()
        obj2 = Base()
        obj = Base(100)

        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj.id, 100)

if __name__ == '__main__':
    unittest.main()
