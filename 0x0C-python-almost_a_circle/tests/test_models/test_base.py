#!/usr/bin/python3
# test module for the class Base
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBaseClass(unittest.TestCase):
    # Test Base Class

    def setUp(self):
        # reset id for each run
        Base._Base__nb_objects = 0

    def test_initial_id(self):
        # test if initializes is okay
        obj1 = Base()
        obj2 = Base()
        obj = Base(100)

        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj.id, 100)

    def test_to_json_string(self):
        # test json representation of object
        list_dicts = [{'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9},
                      {'id': 2, 'width': 5, 'height': 3, 'x': 2, 'y': 4}]
        expected_json = '[{"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}, ' \
                        '{"id": 2, "width": 5, "height": 3, "x": 2, "y": 4}]'
        self.assertEqual(Base.to_json_string(list_dicts), expected_json)

    def test_to_json_string_empty_list(self):
        # test empty list
        list_dicts = []
        expected_json = '[]'
        self.assertEqual(Base.to_json_string(list_dicts), expected_json)

    def test_to_json_string_with_to_dictionary_rec(self):
        # test json string representation using to_dictionary
        rect = Rectangle(10, 5, 2, 3, 1)
        list_dicts = [rect.to_dictionary()]
        expected_json = '[{"x": 2, "y": 3, "id": 1, "height": 5, "width": 10}]'
        self.assertEqual(Base.to_json_string(list_dicts), expected_json)

    def test_to_json_string_with_to_dictionary_sq(self):
         # test json string representation using to_dictionary
        square = Square(10, 2, 1, 1)
        list_dicts = [square.to_dictionary()]
        expected_json = '[{"id": 1, "x": 2, "size": 10, "y": 1}]'
        self.assertEqual(Base.to_json_string(list_dicts), expected_json)

    def test_to_json_string_none(self):
        # test with none
        list_dicts = None
        expected_json = '[]'
        self.assertEqual(Base.to_json_string(list_dicts), expected_json)

    def tearDown(self):
        # Remove created files after each test
        file_names = ["Rectangle.json", "Square.json"]
        for file_name in file_names:
            if os.path.exists(file_name):
                os.remove(file_name)

    def test_save_to_file_rectangle(self):
        # Test save_to_file method with Rectangle objects
        Rectangle._Base__nb_objects = 0

        r1 = Rectangle(10, 20, 1, 1, id=1)
        r2 = Rectangle(5, 5, 2, 2, id=2)
        rectangles = [r1, r2]
        Rectangle.save_to_file(rectangles)

        filename = "Rectangle.json"
        self.assertTrue(os.path.exists(filename))

        with open(filename, 'r') as file:
            content = file.read()
            self.assertEqual(content, '[{"x": 1, "y": 1, "id": 1, "height": 20, "width": 10}, '
                                       '{"x": 2, "y": 2, "id": 2, "height": 5, "width": 5}]')

    def test_save_to_file_rectangle_empty_list(self):
        # Test save_to_file method with an empty list of Rectangle objects
        Rectangle._Base__nb_objects = 0

        rectangles = []
        Rectangle.save_to_file(rectangles)

        filename = "Rectangle.json"
        self.assertTrue(os.path.exists(filename))

        with open(filename, 'r') as file:
            content = file.read()
            self.assertEqual(content, '[]')

    def test_save_to_file_rectangle_none(self):
        # Test save_to_file method with None (no Rectangle objects)
        Rectangle._Base__nb_objects = 0

        rectangles = None
        Rectangle.save_to_file(rectangles)

        filename = "Rectangle.json"
        self.assertTrue(os.path.exists(filename))

        with open(filename, 'r') as file:
            content = file.read()
            self.assertEqual(content, '[]')

    def test_save_to_file_square(self):
        # Test save_to_file method with Square objects
        Square._Base__nb_objects = 0

        s1 = Square(10, 1, 1, 1)
        s2 = Square(5, 2, 2, 2)
        squares = [s1, s2]
        Square.save_to_file(squares)

        filename = "Square.json"
        self.assertTrue(os.path.exists(filename))

        with open(filename, 'r') as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 1, "x": 1, "size": 10, "y": 1}, '
                                       '{"id": 2, "x": 2, "size": 5, "y": 2}]')

    def test_save_to_file_square_empty_list(self):
        # Test save_to_file method with an empty list of Square objects
        Square._Base__nb_objects = 0

        squares = []
        Square.save_to_file(squares)

        filename = "Square.json"
        self.assertTrue(os.path.exists(filename))

        with open(filename, 'r') as file:
            content = file.read()
            self.assertEqual(content, '[]')

    def test_save_to_file_square_none(self):
        # Test save_to_file method with None (no Square objects)
        Square._Base__nb_objects = 0

        squares = None
        Square.save_to_file(squares)

        filename = "Square.json"
        self.assertTrue(os.path.exists(filename))

        with open(filename, 'r') as file:
            content = file.read()
            self.assertEqual(content, '[]')

    def test_from_json_string_empty_string(self):
        # Tests from_json_string with an empty string
        json_string = ""
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_from_json_string_none(self):
        # Tests from_json_string with None
        json_string = None
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_from_json_string_valid_string(self):
        # Tests from_json_string with a valid JSON string
        json_string = '[{"id": 1, "name": "Rectangle", "width": 10, "height": 5}, {"id": 2, "name": "Square", "size": 7}]'
        result = Base.from_json_string(json_string)
        expected = [
            {"id": 1, "name": "Rectangle", "width": 10, "height": 5},
            {"id": 2, "name": "Square", "size": 7}
        ]
        self.assertEqual(result, expected)

    def test_create_square(self):
        # Test create method with Square class
        square_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        square = Square.create(**square_dict)
        self.assertIsInstance(square, Square)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_create_rectangle(self):
        # Test create method with Rectangle class
        rectangle_dict = {'id': 1, 'width': 10, 'height': 5, 'x': 2, 'y': 3}
        rectangle = Rectangle.create(**rectangle_dict)
        self.assertIsInstance(rectangle, Rectangle)
        self.assertEqual(rectangle.id, 1)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 5)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)

    def test_create_invalid_class(self):
        # Test create method with invalid class
        invalid_dict = {'id': 1, 'size': 5, 'x': 2, 'y': 3}
        with self.assertRaises(AttributeError):
            instance = Base.create(**invalid_dict)

    def test_load_from_file_rectangle(self):
        # Test load_from_file method with Rectangle class
        Rectangle._Base__nb_objects = 0

        r1 = Rectangle(10, 20, 1, 1, id=1)
        r2 = Rectangle(5, 5, 2, 2, id=2)
        rectangles = [r1, r2]
        Rectangle.save_to_file(rectangles)

        loaded_rectangles = Rectangle.load_from_file()
        self.assertEqual(len(loaded_rectangles), 2)
        self.assertIsInstance(loaded_rectangles[0], Rectangle)
        self.assertIsInstance(loaded_rectangles[1], Rectangle)
        self.assertEqual(loaded_rectangles[0].id, 1)
        self.assertEqual(loaded_rectangles[1].id, 2)
        self.assertEqual(loaded_rectangles[0].width, 10)
        self.assertEqual(loaded_rectangles[1].width, 5)
        self.assertEqual(loaded_rectangles[0].height, 20)
        self.assertEqual(loaded_rectangles[1].height, 5)
        self.assertEqual(loaded_rectangles[0].x, 1)
        self.assertEqual(loaded_rectangles[1].x, 2)
        self.assertEqual(loaded_rectangles[0].y, 1)
        self.assertEqual(loaded_rectangles[1].y, 2)

    def test_load_from_file_file_not_exist(self):
        # Test load_from_file method when the file doesn't exist
        Square._Base__nb_objects = 0

        filename = "Square.json"
        if os.path.exists(filename):
            os.remove(filename)

        instances = Square.load_from_file()

        self.assertEqual(instances, [])

    def test_load_from_file_file_exists(self):
        # Test load_from_file method when the file exists
        Square._Base__nb_objects = 0

        square = Square(5, 2, 1, 1)
        squares = [square]

        Square.save_to_file(squares)

        instances = Square.load_from_file()

        self.assertEqual(len(instances), 1)
        loaded_square = instances[0]
        self.assertIsInstance(loaded_square, Square)
        self.assertEqual(loaded_square.id, square.id)
        self.assertEqual(loaded_square.size, square.size)
        self.assertEqual(loaded_square.x, square.x)
        self.assertEqual(loaded_square.y, square.y)


if __name__ == '__main__':
    unittest.main()
