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

        with self.assertRaises(TypeError):
            sq = Square(1, "2")

        with self.assertRaises(TypeError):
            sq = Square(1, 4, "2")

        with self.assertRaises(ValueError):
            sq = Square(-1)

        with self.assertRaises(ValueError):
            sq = Square(2, -2)

        with self.assertRaises(ValueError):
            sq = Square(2, 5, -2)

        with self.assertRaises(ValueError):
            sq = Square(0)

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

        """

    def test_update_args_kwargs(self):
        #tests update to rectangle method with args kwargs functionality
        sq = Square(5)
        sq.update(10)
        self.assertEqual(sq.id, 10)

        sq_2 = Square(8)
        sq_2.update(8, 5, 2, 15)
        self.assertEqual(sq_2.id, 8)
        self.assertEqual(sq_2.width, 5)
        self.assertEqual(sq_2.height, 5)
        self.assertEqual(sq_2.x, 2)
        self.assertEqual(sq_2.y, 15)

        sq_3 = Square(5)
        sq_3.update(width=7, x=2)
        self.assertEqual(sq_3.width, 7)
        self.assertEqual(sq_3.height, 7)
        self.assertEqual(sq_3.x, 2)

        sq_4 = Square(8, 2, 3, 12)
        sq_4.update(id=15, height=5, y=8)
        self.assertEqual(sq_4.id, 15)
        self.assertEqual(sq_4.width, 5)
        self.assertEqual(sq_4.height, 5)
        self.assertEqual(sq_4.y, 8)

        sq_5 = Square(4, 5, 6, 7)
        sq_5.update(size=9, x=3, y=9)
        self.assertEqual(sq_5.id, 7)
        self.assertEqual(sq_5.width, 9)
        self.assertEqual(sq_5.height, 9)
        self.assertEqual(sq_5.x, 3)
        self.assertEqual(sq_5.y, 9)

    def test_to_dictionary(self):
        """tests the dictionary representation of Square class"""
        sq = Square(10, 2, 1)
        expected_dic = {'id': sq.id, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(sq.to_dictionary(), expected_dic)


if __name__ == '__main__':
    unittest.main()
