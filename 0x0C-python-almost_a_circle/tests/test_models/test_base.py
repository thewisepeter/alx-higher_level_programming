#!/usr/bin/python3
#test module for the class Base
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseClass(unittest.TestCase):
    #Test Base Class

    def test_initial_id(self):
        obj1 = Base()
        obj2 = Base()
        obj = Base(100)

        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj.id, 100)

    def test_to_json_string(self):
        list_dicts = [{'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9},
                      {'id': 2, 'width': 5, 'height': 3, 'x': 2, 'y': 4}]
        expected_json = '[{"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}, ' \
                        '{"id": 2, "width": 5, "height": 3, "x": 2, "y": 4}]'
        self.assertEqual(Base.to_json_string(list_dicts), expected_json)

    def test_to_json_string_empty_list(self):
        list_dicts = []
        expected_json = '[]'
        self.assertEqual(Base.to_json_string(list_dicts), expected_json)

    def test_to_json_string_with_to_dictionary_rec(self):
        rect = Rectangle(10, 5, 2, 3, 1)
        list_dicts = [rect.to_dictionary()]
        expected_json = '[{"x": 2, "y": 3, "id": 1, "height": 5, "width": 10}]'
        self.assertEqual(Base.to_json_string(list_dicts), expected_json)

    def test_to_json_string_with_to_dictionary_sq(self):
        square = Square(10, 2, 1, 1)
        list_dicts = [square.to_dictionary()]
        expected_json = '[{"id": 1, "x": 2, "size": 10, "y": 1}]'
        self.assertEqual(Base.to_json_string(list_dicts), expected_json)

    def test_to_json_string_none(self):
        list_dicts = None
        expected_json = '[]'
        self.assertEqual(Base.to_json_string(list_dicts), expected_json)


if __name__ == '__main__':
    unittest.main()
