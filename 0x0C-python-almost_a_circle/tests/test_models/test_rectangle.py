#!/usr/bin/python3
#test module for the class Rectangle
import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
from unittest import mock


class TestRectangle(unittest.TestCase):
    #Test Rectangle Class

    def test_initial_values(self):
        #tests if initiation is done right
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

    def test_attribute_validation(self):
        #test for validation of attributes of rectangle class
        with self.assertRaises(TypeError):
            rec = Rectangle(2, "3", 4, 6)

        with self.assertRaises(TypeError):
            rec = Rectangle("2", 3, 4, 6)

        with self.assertRaises(ValueError):
            rec = Rectangle(-2, 3, 4, 6)

        with self.assertRaises(ValueError):
            rec = Rectangle(2, -3, 4, 6)

        with self.assertRaises(TypeError):
            rec = Rectangle(2, 3, "4", 6)

        with self.assertRaises(TypeError):
            rec = Rectangle(2, 3, 4, "6")

        with self.assertRaises(ValueError):
            rec = Rectangle(2, 3, -4, 6)

        with self.assertRaises(ValueError):
            rec = Rectangle(2, 3, 4, -6)

    def test_area(self):
        #test for area function of rectangle class
        rec = Rectangle(5, 4)
        self.assertEqual(rec.area(), 20)

        rec.width = 8
        rec.height = 5
        self.assertEqual(rec.area(), 40)

    def test_display(self):
        #tests the display function of rectangle class
        rec = Rectangle(4, 3)

        expected_display = "####\n" \
                           "####\n" \
                           "####\n"

        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            rec.display()
            self.assertEqual(fake_out.getvalue(), expected_display)


if __name__ == '__main__':
    unittest.main()