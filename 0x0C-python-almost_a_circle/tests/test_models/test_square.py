#!/usr/bin/python3
#test module for the class Square
import unittest
from models.square import Square
from io import StringIO
from unittest import mock


class TestRectangle(unittest.TestCase):
    #Test Rectangle Class

    def test_initial_values(self):
        #tests if initiation is done right
        sq = Square(5)
        self.assertEqual(sq.width, 5)
        self.assertEqual(sq.height, 5)
        self.assertEqual(sq.x, 0)
        self.assertEqual(sq.y, 0)
        self.assertIsNotNone(sq.id)

        sq_2 = Square(10, 2, 3, 15)
        self.assertEqual(sq_2.width, 10)
        self.assertEqual(sq_2.height, 10)
        self.assertEqual(sq_2.x, 2)
        self.assertEqual(sq_2.y, 3)
        self.assertIsNotNone(sq_2.id, 15)

    def test_attribute_validation(self):
        #test for validation of attributes of Square class
        with self.assertRaises(TypeError):
            sq = Square("3")

        with self.assertRaises(TypeError):
            sq = Square(2 + 3j)

    """def test_area(self):
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
            self.assertEqual(fake_out.getvalue(), expected_display)"""

    def test_str(self):
        #tests the str method of the square class
        sq = Square(5, 2, 3, 7)
        expected_str = '[Square] (7) 2/3 - 5'
        self.assertEqual(str(sq), expected_str)

        sq_2 = Square(9)
        expected_str = '[Square] ({}) 0/0 - 9'.format(sq_2.id)
        self.assertEqual(str(sq_2), expected_str)

    """def test_display_with_coord(self):
        #tests the display function of rectangle class with coordinates
        rec = Rectangle(5, 3, 2, 1)

        expected_display = "\n  #####\n" \
                           "  #####\n" \
                           "  #####\n"

        with mock.patch('sys.stdout', new=StringIO()) as fake_out:
            rec.display()
            self.assertEqual(fake_out.getvalue(), expected_display)

    def test_update_args(self):
        #tests update to rectangle method with only args
        rec = Rectangle(5, 10, 2, 4, id=1)

        self.assertEqual(rec.width, 5)
        self.assertEqual(rec.height, 10)
        self.assertEqual(rec.x, 2)
        self.assertEqual(rec.y, 4)
        self.assertEqual(rec.id, 1)

        rec.update(1, 3, 5, 6, 4)

        self.assertEqual(rec.id, 1)
        self.assertEqual(rec.width, 3)
        self.assertEqual(rec.height, 5)
        self.assertEqual(rec.x, 6)
        self.assertEqual(rec.y, 4)

    def test_update_args_kwargs(self):
        #tests update to rectangle method with args kwargs functionality
        rec = Rectangle(5, 10, 2, 4, id=1)
        self.assertEqual(str(rec), "[Rectangle] (1) 2/4 - 5/10")

        rec.update(2)
        self.assertEqual(str(rec), "[Rectangle] (2) 2/4 - 5/10")

        rec.update(3, 4)
        self.assertEqual(str(rec), "[Rectangle] (3) 2/4 - 4/10")

        rec.update(4, 5, 7)
        self.assertEqual(str(rec), "[Rectangle] (4) 2/4 - 5/7")

        rec.update(7, 6, 3, 5)
        self.assertEqual(str(rec), "[Rectangle] (7) 5/4 - 6/3")

        rec.update(width=10)
        self.assertEqual(str(rec), "[Rectangle] (7) 5/4 - 10/3")

        rec.update(y=7, height=49)
        self.assertEqual(str(rec), "[Rectangle] (7) 5/7 - 10/49")

        rec.update(id=6, x=7, width=3, y=7, height=10)
        self.assertEqual(str(rec), "[Rectangle] (6) 7/7 - 3/10")

        rec.update(width=34, id=9, x=8)
        self.assertEqual(str(rec), "[Rectangle] (9) 8/7 - 34/10")

        rec.update(3, height=6, y=4)
        self.assertEqual(str(rec), "[Rectangle] (3) 8/7 - 34/10")"""


if __name__ == '__main__':
    unittest.main()
