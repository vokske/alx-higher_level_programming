#!/usr/bin/python3
"""Module contain class TestRectangle."""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch
from contextlib import redirect_stdout


class TestRectangle(unittest.TestCase):
    """Test functions for the class Rectangle."""

    def setUp(self):
        """Reset object Id variable before each test function."""

        Base._Base__nb_objects = 0

    def test_rect_is_base(self):
        """Tests if Rectangle is an instance of Base."""

        self.assertIsInstance(Rectangle(4, 6), Base)
        self.assertIsNot(Rectangle(4, 6), Base)

    def test_rect_initialization(self):
        """Tests rectangle initialization."""

        r = Rectangle(4, 6)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 6)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 1)

    def test_rect_init_with_id(self):
        """Test Rectangle initializationwith Id."""

        r = Rectangle(3, 8, 1, 2, 13)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 13)

    def test_rect_init_without_id(self):
        """Test Rectangle initialization without Id."""

        r = Rectangle(3, 8, 1, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 1)
        r1 = Rectangle(4, 7, 3, 5)
        self.assertEqual(r1.width, 4)
        self.assertEqual(r1.height, 7)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 2)

    def test_getter_setter(self):
        """Test the attribute getters and setters."""

        r = Rectangle(4, 6, 2, 3)
        r.width = 5
        r.height = 7
        r.x = 4
        r.y = 1
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 7)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 1)

    def test_type_error(self):
        """Test type validation for width, height, x, and y."""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("5", 3)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(4, [3])

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, complex(3))

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float("NaN"), 6)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(23, float("inf"))

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(14, (3,))

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, {})

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 4)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(18, 4.5)

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("2", 5)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(3, 7, "5")

    def test_value_error(self):
        """Tests proper raising of a ValueError."""

        with self.assertRaises(ValueError) as ve:
            Rectangle(-3, 4)
        self.assertEqual(str(ve.exception), "width must be > 0")

        with self.assertRaises(ValueError) as ve:
            Rectangle(0, 4)
        self.assertEqual(str(ve.exception), "width must be > 0")

        with self.assertRaises(ValueError) as ve:
            Rectangle(4, 0)
        self.assertEqual(str(ve.exception), "height must be > 0")

        with self.assertRaises(ValueError) as ve:
            Rectangle(4, -2)
        self.assertEqual(str(ve.exception), "height must be > 0")

        with self.assertRaises(ValueError) as ve:
            Rectangle(6, 2, -5)
        self.assertEqual(str(ve.exception), "x must be >= 0")

        with self.assertRaises(ValueError) as ve:
            Rectangle(10, 4, 5, -4)
        self.assertEqual(str(ve.exception), "y must be >= 0")

    def test_area_method(self):
        """Tests the area method of an instance of Rectangle."""

        a = Rectangle(4, 5, 2, 3)
        self.assertEqual(a.area(), 20)
        a1 = Rectangle(7, 10000000000000000000000000000)
        self.assertEqual(a1.area(), (7 * 10000000000000000000000000000))

    def test_display(self):
        """Tests the dispay method of an instance of Rectangle."""

        r1 = Rectangle(4, 5)
        expected_output = "####\n####\n####\n####\n####\n"
        with patch("sys.stdout", new=StringIO()) as rect_out:
            r1.display()
            self.assertEqual(rect_out.getvalue(), expected_output)

        r2 = Rectangle(9, 11)
        expected_output = '#########\n#########\n#########\n#########\
\n#########\n#########\n#########\n#########\n#########\n\
#########\n#########\n'
        with patch("sys.stdout", new=StringIO()) as rect_out:
            r2.display()
            self.assertEqual(rect_out.getvalue(), expected_output)

        r3 = Rectangle(4, 3, 2, 1)
        expected_output = "\n  ####\n  ####\n  ####\n"
        with StringIO() as buf, redirect_stdout(buf):
            r3.display()
            self.assertEqual(buf.getvalue(), expected_output)

        r4 = Rectangle(2, 2, 3, 2)
        expected_output = "\n\n   ##\n   ##\n"
        with StringIO() as buf, redirect_stdout(buf):
            r4.display()
            self.assertEqual(buf.getvalue(), expected_output)

    def test_str_method(self):
        """Checks the string representation of a Rectangle instance."""

        r = Rectangle(4, 6)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 4/6")
        r.update(10, 15, 5, 5)
        self.assertEqual(str(r), "[Rectangle] (10) 5/0 - 15/5")

        r1 = Rectangle(12, 14)
        self.assertEqual(str(r1), "[Rectangle] (2) 0/0 - 12/14")
        r1.update(x=3, width=33, y=4, height=11)
        self.assertEqual(str(r1), "[Rectangle] (2) 3/4 - 33/11")

    def test_update_with_args(self):
        """Check that Rectangle instance is correctly updated with args."""

        r = Rectangle(4, 8, 3, 4, 13)
        r.update()
        self.assertEqual(r.id, 13)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

        r1 = Rectangle(5, 7)
        r1.update(6, 8, 2, 3)
        self.assertEqual(r1.id, 6)
        self.assertEqual(r1.width, 8)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(12, 18)
        r2.update()
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 12)
        self.assertEqual(r2.height, 18)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        r3 = Rectangle(10, 23, 3, 4)
        r3.update(1)
        self.assertEqual(r3.id, 1)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 23)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)

        r4 = Rectangle(10, 15, 20, 5, 5)
        r4.update(15, 20, 25, 6, 6)
        self.assertEqual(r4.id, 15)
        self.assertEqual(r4.width, 20)
        self.assertEqual(r4.height, 25)
        self.assertEqual(r4.x, 6)
        self.assertEqual(r4.y, 6)

    def test_update_with_kwargs(self):
        """Test updating attributes using kwargs."""

        r = Rectangle(5, 6, 4, 4, 10)
        r.update(id=45, width=15, height=20, x=5, y=8)
        self.assertEqual(r.id, 45)
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 8)

        r1 = Rectangle(15, 20, 30, 10, 5)
        r1.update(id=94, width=32, height=24, x=4)
        self.assertEqual(r1.id, 94)
        self.assertEqual(r1.width, 32)
        self.assertEqual(r1.height, 24)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 10)

        r2 = Rectangle(5, 8, 2, 3, 50)
        r2.update(id=55, width=10, height=5)
        self.assertEqual(r2.id, 55)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 5)
        self.assertEqual(r2.x, 2)
        self.assertEqual(r2.y, 3)

        r3 = Rectangle(12, 24, 5, 6)
        r3.update(width=10, id=5, x=2, height=9, y=3)
        self.assertEqual(r3.id, 5)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 9)
        self.assertEqual(r3.x, 2)
        self.assertEqual(r3.y, 3)

        r4 = Rectangle(12, 18)
        r4.update(x=5, height=15, width=11)
        self.assertEqual(r4.id, 2)
        self.assertEqual(r4.width, 11)
        self.assertEqual(r4.height, 15)
        self.assertEqual(r4.x, 5)
        self.assertEqual(r4.y, 0)

    def test_args_over_kwargs(self):
        """Test that args take precedence over kwargs."""

        r = Rectangle(3, 5, 4, 2, 1)
        r.update(5, 6, 4, 4, 8, id=40, width=10, height=9, x=2, y=3)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 8)

        r1 = Rectangle(10, 5, 3, 3, 23)
        r1.update(15, 8, 4, id=40, width=10, height=9, x=2, y=3)
        self.assertEqual(r1.id, 15)
        self.assertEqual(r1.width, 8)
        self.assertEqual(r1.height, 4)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 3)

        r2 = Rectangle(7, 5)
        r2.update(13, 9, 8, id=40, width=10, height=9, x=2, y=3)
        self.assertEqual(r2.id, 13)
        self.assertEqual(r2.width, 9)
        self.assertEqual(r2.height, 8)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)

        r3 = Rectangle(12, 18, 3, 2, 7)
        r.update(5, 6, 4, 4, 8, id=40, width=10, height=9, x=2, y=3)
        self.assertEqual(r.id, 5)
        self.assertEqual(r.width, 6)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 8)

    def test_rect_to_dict(self):
        """Checks if instance is correctly represented as a dictionary."""

        r = Rectangle(5, 8, 3, 3, 6)
        self.assertEqual(r.to_dictionary(),
                         {"id": 6, "width": 5, "height": 8, "x": 3, "y": 3})

        r1 = Rectangle(12, 15)
        self.assertEqual(r1.to_dictionary(),
                         {"width": 12, "x": 0, "height": 15, "id": 1, "y": 0})

    def test_create_rectangle(self):
        """Check if an instance is correctly created from dictionary."""

        r = Rectangle(15, 12, 3, 4)
        r_dict = r.to_dictionary()
        r1 = Rectangle.create(**r_dict)
        self.assertEqual(r1.id, r.id)
        self.assertEqual(r1.width, r.width)
        self.assertEqual(r1.y, r.y)
        self.assertEqual(r1.x, r.x)
        self.assertEqual(r1.height, r.height)

        r2 = Rectangle(5, 8)
        r2_dict = r2.to_dictionary()
        r3 = Rectangle.create(**r2_dict)
        self.assertEqual(r3.height, r2.height)
        self.assertEqual(r3.id, r2.id)
        self.assertEqual(r3.width, r2.width)
        self.assertEqual(r3.x, r2.x)
        self.assertEqual(r3.y, r2.y)


if __name__ == "__main__":
    unittest.main()
