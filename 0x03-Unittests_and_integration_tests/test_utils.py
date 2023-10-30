#!/usr/bin/env python3
""" Task 0: Module"""

import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import get_json, access_nested_map, memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Class for testing Nested Map function """
    @parameterized.expand([
       ({"a": 1}, ("a",), 1),
       ({"a": {"b": 2}}, ("a",), {"b": 2}),
       ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test method return output """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """ Test method raises correct exception """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(cm.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """ Class for testing get_json function """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ Test method returns correct output """
        mock_get.return_value.json.return_value = test_payload

        response = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """ Class for testing memoization """

    def test_memoize(self):
        """ Tests memoize function """
        class TestClass:
            """ Test class """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_a_method:
            test_obj = TestClass()

            # Call a_property twice
            res1 = test_obj.a_property
            res2 = test_obj.a_property

            # Check that the correct result is returned
            self.assertEqual(res1, 42)
            self.assertEqual(res2, 42)

            # Check that a_method is only called once
            mock_a_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
