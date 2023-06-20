#!/usr/bin/python3
#test module for the class Rectangle
import unittest
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

        with self.assertRaises(ValueError):
            rec = Rectangle(0, 2)

        with self.assertRaises(ValueError):
            rec = Rectangle(1, 0)

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

    def test_str(self):
        #tests the str method of the rectangle class
        rec = Rectangle(5, 4, 2, 3, id=1)

        expected_str = '[Rectangle] (1) 2/3 - 5/4'

        self.assertEqual(str(rec), expected_str)

    def test_display_with_coord(self):
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
        self.assertEqual(str(rec), "[Rectangle] (3) 8/7 - 34/10")

    def test_to_dictionary(self):
        """tests the dictionary representation of the rectangle"""
        rec = Rectangle(10, 2, 1, 9)
        expected_dic = {'x': 1, 'y': 9, 'id': rec.id, 'height': 2, 'width': 10}
        self.assertEqual(rec.to_dictionary(), expected_dic)



if __name__ == '__main__':
    unittest.main()
