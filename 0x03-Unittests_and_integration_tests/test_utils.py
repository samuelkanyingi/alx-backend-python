#!/usr/bin/env python3
"""
Unit tests for the access_nested_map function
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map  # Make sure the import path is correct

class TestAccessNestedMap(unittest.TestCase):
    """
    Unit test class for the access_nested_map function.
    """
    
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test the access_nested_map function with various inputs.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

if __name__ == '__main__':
    unittest.main()
