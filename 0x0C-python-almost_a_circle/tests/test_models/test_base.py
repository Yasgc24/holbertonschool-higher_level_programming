#!/usr/bin/python3
"""Test models.base"""
from models.base import Base
import unittest

class TestClassBase(unittest.TestCase):
    """Tests for the Base class"""

    def test_none_id(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)
        self.assertEqual(Base().id, 4)
        self.assertEqual(Base().id, 5)

    def test_positive_id(self):
        self.assertEqual(Base(0).id, 0)
        self.assertEqual(Base(1).id, 1)
        self.assertEqual(Base(2).id, 2)
        self.assertEqual(Base(3).id, 3)
        self.assertEqual(Base(12).id, 12)
    
    def test_negative_id(self):
        self.assertEqual(Base(-1).id, -1)
        self.assertEqual(Base(-2).id, -2)
        self.assertEqual(Base(-3).id, -3)
        self.assertEqual(Base(-12).id, -12)
        self.assertEqual(Base(-100).id, -100)


if __name__ == "__main__":
    unittest.main()