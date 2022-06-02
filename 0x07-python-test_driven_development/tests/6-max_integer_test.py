#!/usr/bin/python3
"""
5. Max integer - Unittest
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
        """Test cases"""
        
        def max_at_end(self):
            list = [10, 20, 30, 40]
            self.assertEqual(max_integer(list),40)

        def max_at_beggining(self):
            list = [40, 30, 20, 10]
            self.assertEqual(max_integer(list), 40)
    
        def max_in_middle(self):
            list = [5, 10, 15, 12, 8, 4]
            self.assertEqual(max_integer(list), 15)

        def one_negative(self):
            list = [0, -20, 40, 60]
            self.assertEqual(max_integer(list), 60)

        def negative_numbers(self):
            list = [-2, -4, -6, -8]
            self.assertEqual(max_integer(list), -2)

        def one_element(self):
            list = [5]
            self.assertEqual(max_integer(list), 5)

        def list_empty(self):
            list = []
            self.assertEqual(max_integer(list), None)
