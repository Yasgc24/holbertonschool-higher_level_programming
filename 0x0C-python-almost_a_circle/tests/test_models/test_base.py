#!/usr/bin/python3
"""Test models.base"""
from models.base import Base
import unittest

class TestClassBase(unittest.TestCase):
    """Tests for the Base class"""

    def test_none_id(self):
        """Test none value for id"""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)
        self.assertEqual(Base().id, 4)
        self.assertEqual(Base().id, 5)

    def test_positive_id(self):
        """Test positive number for id"""
        self.assertEqual(Base(0).id, 0)
        self.assertEqual(Base(1).id, 1)
        self.assertEqual(Base(2).id, 2)
        self.assertEqual(Base(3).id, 3)
        self.assertEqual(Base(12).id, 12)
    
    def test_negative_id(self):
        """Test negative number for id"""
        self.assertEqual(Base(-1).id, -1)
        self.assertEqual(Base(-2).id, -2)
        self.assertEqual(Base(-3).id, -3)
        self.assertEqual(Base(-12).id, -12)
        self.assertEqual(Base(-100).id, -100)

    def test_float_id(self):
        """Test float number for id"""
        self.assertEquals(Base(3.5).id, 3.5)
        self.assertEqual(Base(7.4).id, 7.4)
        self.assertEqual(Base(-5.3).id, -5.3)
        self.assertEqual(Base(-100.6).id, -100.6)
        self.assertEqual(Base(4.2).id, 4.2)

    def test_floantinf_id(self):
        """Test float inf number for id"""
        self.assertEqual(Base(float('inf')).id, float('inf'))

    def test_dict_id(self):
        """Test dictinionary as value for id"""
        self.assertEqual(Base({"num1": 3, "num2": 4}).id, {"num1": 3, "num2": 4})

    def test_list_id(self):
        """Test list as value for id"""
        self.assertEqual(Base([1, 2, 3]).id, [1, 2, 3])

    

if __name__ == "__main__":
    unittest.main()