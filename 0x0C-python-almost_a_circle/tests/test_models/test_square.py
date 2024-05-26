#!/usr/bin/python3
"""Module contains unittests for the class Square."""

import unittest
from models.base import Base
from models.square import Square


class TestSquare(unittest.TestCase):
    """Contains various test functions for the class Square."""

    def setUp(self):
        """Reset the instance count after each test."""

        Base._Base__nb_objects = 0

    def test_init_square(self):
        """Test the initialization of a Square instance."""

        s = Square(6)
        self.assertEqual(s.width, 6)
        self.assertEqual(s.height, 6)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 1)

        s1 = Square(6, 4, 5, 9)
        self.assertEqual(s1.width, 6)
        self.assertEqual(s1.height, 6)
        self.assertEqual(s1.x, 4)
        self.assertEqual(s1.y, 5)
        self.assertEqual(s1.id, 9)

        s2 = Square(12, 3, 5)
        self.assertEqual(s2.width, 12)
        self.assertEqual(s2.height, 12)
        self.assertEqual(s2.x, 3)
        self.assertEqual(s2.y, 5)
        self.assertEqual(s2.id, 2)

    def test_with_error(self):
        """Tests to check handling of bad values."""

        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-4, 3, 4, 56)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(12, 0, 0.5)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(20, -3, -1, 10)

    def test_square_str(self):
        """Check that __str__ method displays Square object correctly."""

        s = Square(6, 4, 4, 10)
        self.assertEqual(str(s), "[Square] (10) 4/4 - 6")

        s1 = Square(10)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 10")

        s2 = Square(14)
        s2.update(4, 20)
        self.assertEqual(str(s2), "[Square] (4) 0/0 - 20")

        s3 = Square(7, 3, 2)
        s3.update(size=17)
        self.assertEqual(str(s3), "[Square] (3) 3/2 - 17")

    def test_square_getter_setter(self):
        """Check that the Square getter and setter works correctly."""

        s = Square(10)
        self.assertEqual(s.size, 10)
        s.size = 15
        self.assertEqual(s.size, 15)
        self.assertEqual(s.width, 15)
        self.assertEqual(s.height, 15)

        s1 = Square(100, 4, 5)
        self.assertEqual(s1.size, 100)
        s1.size = 45
        s1.x = 12
        s1.y = 10
        self.assertEqual(s1.size, 45)
        self.assertEqual(s1.width, 45)
        self.assertEqual(s1.height, 45)
        self.assertEqual(s1.x, 12)
        self.assertEqual(s1.y, 10)

    def test_square_update_args_kwargs(self):
        """Test how args and kwargs update a Square instance."""

        s = Square(16)
        s.update(18, 3, 5)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.width, 3)
        self.assertEqual(s.height, 3)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 18)

        s1 = Square(30, 3, 4, 15)
        s1.update(x=0, size=20, id=3, y=1)
        self.assertEqual(s1.id, 3)
        self.assertEqual(s1.size, 20)
        self.assertEqual(s1.width, 20)
        self.assertEqual(s1.height, 20)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 1)

        s2 = Square(18, 5, 5)
        s2.update(2, 15, x=8, id=23, size=25)
        self.assertEqual(s2.size, 15)
        self.assertEqual(s2.x, 5)
        self.assertEqual(s2.id, 2)
        self.assertEqual(s2.y, 5)
        self.assertEqual(s2.height, 15)
        self.assertEqual(s2.width, 15)

    def test_square_to_dict(self):
        """Check the dictionary representation of a Square instance."""

        s = Square(8, 4, 4)
        self.assertEqual(s.to_dictionary(),
                         {"id": 1, "size": 8, "x": 4, "y": 4})

        s1 = Square(12, 15)
        self.assertEqual(s1.to_dictionary(),
                         {"size": 12, "id": 2, "y": 0, "x": 15})

    def test_create_square(self):
        """Check if a Square instance is correctly created from dictionary."""

        s = Square(6)
        s_dict = s.to_dictionary()
        s1 = Square.create(**s_dict)
        self.assertEqual(s.size, s1.size)
        self.assertEqual(s.id, s1.id)
        self.assertEqual(s.width, s1.width)
        self.assertEqual(s.height, s1.height)
        self.assertEqual(s.x, s1.x)
        self.assertEqual(s.y, s1.y)


if __name__ == "__main__":
    unittest.main()
