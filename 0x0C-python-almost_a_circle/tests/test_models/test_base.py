#!/usr/bin/python3
"""Contains unittests for the class Base."""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
from unittest.mock import patch


class TestBase(unittest.TestCase):
    """Test functions for the class Base."""

    def setUp(self):
        """Reset the __nb_obects counter before each test for isolation."""

        Base._Base__nb_objects = 0

    def tearDown(self):
        """Cleanup files after each test."""

        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def test_no_id(self):
        """Check id when creating an instance with no id."""

        b = Base()
        b1 = Base()
        b2 = Base()
        self.assertEqual(b.id, 1)
        self.assertEqual(b1.id, 2)
        self.assertEqual(b2.id, 3)

    def test_with_id(self):
        """Creating instances with specific Id."""

        b = Base(40)
        b1 = Base(75)
        b2 = Base(101)
        self.assertEqual(b.id, 40)
        self.assertEqual(b1.id, 75)
        self.assertEqual(b2.id, 101)

    def test_mixed_id(self):
        """Creating instances with and without Id."""

        b = Base()
        b1 = Base(34)
        b2 = Base()
        b3 = Base(72)
        self.assertEqual(b.id, 1)
        self.assertEqual(b1.id, 34)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 72)

    def test_none_id(self):
        """Testing instances with the Id 'None'."""

        b = Base(None)
        b1 = Base(None)
        self.assertEqual(b.id, 1)
        self.assertEqual(b1.id, 2)

    def test_large_number(self):
        """Test an instance of Base with a large number."""

        large = 230000000000000000
        b = Base(large)
        self.assertEqual(b.id, large)

    def test_dict_to_json_str(self):
        """Test method that converts list_dictionaries to JSON string."""

        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")

        list_dict = [{"id": 1, "width": 10}, {"id": 4, "height": 15}]
        result = '[{"id": 1, "width": 10}, {"id": 4, "height": 15}]'
        self.assertEqual(Base.to_json_string(list_dict), result)

        r = Rectangle(12, 10)
        dict1 = r.to_dictionary()
        expected = '{"id": 1, "width": 12, "height": 10, "x": 0, "y": 0}'
        self.assertEqual(Base.to_json_string(dict1), expected)

    def test_save_to_file_rect(self):
        """Test writing of JSON representation of list_objs to a file."""

        r = Rectangle(12, 16, 2, 4, 1)
        r1 = Rectangle(18, 24, 3, 5, 2)
        Rectangle.save_to_file([r, r1])
        with open("Rectangle.json", "r") as f:
            content = f.read()
        expected = Base.to_json_string([r.to_dictionary(), r1.to_dictionary()])
        self.assertEqual(content, expected)

    def test_save_to_file_square(self):
        """Test writing of JSON representation of list_objs to a file."""

        s = Square(15, 2, 4, 1)
        s1 = Square(24, 3, 5, 2)
        Square.save_to_file([s, s1])
        with open("Square.json", "r") as f:
            content = f.read()
        expected = Base.to_json_string([s.to_dictionary(), s1.to_dictionary()])
        self.assertEqual(content, expected)

        Square.save_to_file([])
        with open("Square.json", "r") as f:
            content = f.read()
        self.assertEqual(content, "[]")

        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            stuff = f.read()
        self.assertEqual(stuff, "[]")

    def test_from_json_string(self):
        """Checks conversion from JSON string to list of instances."""

        json_str = '[{"id": 1, "width": 15, "height": 10, "x": 2, "y": 4}]'
        result = Base.from_json_string(json_str)
        expected = [{"id": 1, "width": 15, "height": 10, "x": 2, "y": 4}]
        self.assertEqual(result, expected)

        result_1 = Base.from_json_string("")
        self.assertEqual(result_1, [])

        result_2 = Base.from_json_string(None)
        self.assertEqual(result_2, [])

    def test_load_from_file_rect(self):
        """Test JSON deserialization."""

        r = Rectangle(20, 30)
        r1 = Rectangle(10, 15)
        Rectangle.save_to_file([r, r1])
        rect = Rectangle.load_from_file()
        self.assertEqual(len(rect), 2)
        self.assertEqual(rect[0].id, 1)
        self.assertEqual(rect[1].id, 2)

        Rectangle.save_to_file(None)
        rect1 = Rectangle.load_from_file()
        self.assertEqual(rect1, [])

        Square.save_to_file(None)
        sq1 = Square.load_from_file()
        self.assertEqual(sq1, [])

        s = Square(20, 4, 5, 2)
        s1 = Square(10, 5, 5, 3)
        Square.save_to_file([s, s1])
        sq = Square.load_from_file()
        self.assertEqual(len(sq), 2)
        self.assertEqual(sq[0].id, 2)
        self.assertEqual(sq[1].id, 3)

    def test_save_to_file_csv(self):
        """Test serialization in CSV."""
        r = Rectangle(10, 15, 2, 3)
        r1 = Rectangle(12, 14, 1, 2, 3)
        Rectangle.save_to_file_csv([r, r1])
        with open("Rectangle.csv", "r") as f:
            content = f.read()
        expected = "1,10,15,2,3\n3,12,14,1,2\n"
        self.assertEqual(content, expected)

        s = Square(15, 1, 2, 3)
        s1 = Square(25, 2, 3, 5)
        Square.save_to_file_csv([s, s1])
        with open("Square.csv", "r") as f:
            content = f.read()
        expected = "3,15,1,2\n5,25,2,3\n"
        self.assertEqual(content, expected)

    def test_load_from_file_csv(self):
        """Test deserialization in CSV."""
        r = Rectangle(10, 9, 2, 4, 1)
        r1 = Rectangle(12, 6, 1, 1, 2)
        Rectangle.save_to_file_csv([r, r1])
        rect = Rectangle.load_from_file_csv()
        self.assertEqual(len(rect), 2)
        self.assertEqual(rect[0].id, 1)
        self.assertEqual(rect[1].id, 2)
        self.assertEqual(rect[0].width, 10)
        self.assertEqual(rect[1].y, 1)

        s = Square(15, 1, 2, 3)
        s1 = Square(7, 2, 3, 4)
        Square.save_to_file_csv([s, s1])
        sq = Square.load_from_file_csv()
        self.assertEqual(len(sq), 2)
        self.assertEqual(sq[0].id, 3)
        self.assertEqual(sq[1].id, 4)
        self.assertEqual(sq[0].size, 15)
        self.assertEqual(sq[1].width, 7)
        self.assertEqual(sq[1].x, 2)

        Rectangle.save_to_file_csv("")
        rect1 = Rectangle.load_from_file_csv()
        self.assertEqual(rect1, [])


if __name__ == "__main__":
    unittest.main()
