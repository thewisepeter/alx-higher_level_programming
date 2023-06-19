#!/usr/bin/python3
#test module for the class Rectangle
import unittest
from models.base import Base
from models.rectangle import Rectangle 


class TestRectangle(unittest.TestCase):
    #Test Rectangle Class

    def test_initial_values(self):
        rec = Rectangle(5, 10, 2, 4, id=1)

        self.assertEqual(rec.width, 5)
        self.assertEqual(rec.height, 10)
        self.assertEqual(rec.x, 2)
        self.assertEqual(rec.y, 4)
        self.assertEqual(rec.id, 1)

        rec.width = 4
        rec.height = 7
        rec.x = 1
        rec.y = 9
        rec.id = 5

        self.assertEqual(rec.width, 4)
        self.assertEqual(rec.height, 7)
        self.assertEqual(rec.x, 1)
        self.assertEqual(rec.y, 9)
        self.assertEqual(rec.id, 5)

if __name__ == '__main__':
    unittest.main()
