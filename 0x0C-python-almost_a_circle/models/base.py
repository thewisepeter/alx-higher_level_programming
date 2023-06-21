#!/usr/bin/python3
"""module of the class Base"""
import json
import csv
#import turtle


class Base:
    """this is the base class from which others inherit"""
    __nb_objects = 0
    """turtle.setup(800, 600)
    turtle.bgcolor("white")
    turtle.title("Shapes")"""

    def __init__(self, id=None):
        """ initiation method
        args:
            id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file."""
        if list_objs is None:
            list_objs = []

        file_name = cls.__name__ + ".json"
        json_data = cls.to_json_string([obj.to_dictionary()
                                        for obj in list_objs])

        with open(file_name, "w") as a_file:
            a_file.write(json_data)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, "r") as a_file:
                json_str = a_file.read()
                obj_list = cls.from_json_string(json_str)
                instances = [cls.create(**obj) for obj in obj_list]
                return instances
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        #saves object instance to cls file
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            if list_objs is not None:
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                    elif cls.__name__ == "Square":
                        writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        #loads object from cls file
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                instances = []
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls.create(width=int(row[1]), height=int(row[2]), x=int(row[3]), y=int(row[4]))
                    elif cls.__name__ == "Square":
                        instance = cls.create(size=int(row[1]), x=int(row[2]), y=int(row[3]))
                    instances.append(instance)
                return instances
        except FileNotFoundError:
            return []

    """@staticmethod
    def draw(list_rectangles, list_squares):
        #draw shapes using turtle
        window = turtle.Screen()
        window.bgcolor("white")
        t = turtle.Turtle()
        t.speed(5)
        for rec in list_rectangles:
            width = rec.width
            height = rec.height
            for i in range(2):
                t.forward(width)
                t.left(90)
                t.forward(height)
                t.left(90)

        for sq in list_squares:
            size = sq.size
            for i in range(4):
                t.forward(size)
                t.left(90)
        turtle.done()"""
