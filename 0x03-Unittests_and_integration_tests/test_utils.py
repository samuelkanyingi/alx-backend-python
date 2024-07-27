#!/usr/bin/env python3
"""
Unit tests for the get_value function
"""

import unittest
from typing import Dict, Any, Tuple

def get_value(nested_map: Dict[str, Any], path: Tuple[str, ...]) -> Any:
    """
    Retrieve the value from a nested dictionary using a given path of keys.
    
    Args:
        nested_map (Dict[str, Any]): The nested dictionary to search.
        path (Tuple[str, ...]): The path of keys to follow.
    
    Returns:
        Any: The value at the end of the path.
    """
    for key in path:
        nested_map = nested_map[key]
    return nested_map

class TestGetValue(unittest.TestCase):
    """
    Unit test class for the get_value function.
    """
    
    def test_get_value(self):
        """
        Test the get_value function with various inputs.
        """
        self.assertEqual(get_value({"a": {"b": 2}}, ("a",)), {"b": 2})
        self.assertEqual(get_value({"a": {"b": 2}}, ("a", "b")), 2)

if __name__ == '__main__':
    unittest.main()

