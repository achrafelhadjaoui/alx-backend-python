#!/usr/bin/env python3
"""Unit tests for utility functions used in various applications."""
import unittest
from parameterized import parameterized
from utils import *
from typing import Any, Tuple, Dict
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
        Tests for the access_nested_map function, which retrieves
        values from nested dictionaries.
    """

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Dict[str, Any], path: Tuple[str], expected: Any
    ) -> None:
        """
            Test that access_nested_map returns the correct value
            based on a specified path.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(
        self, nested_map: Dict[str, Any], path: Tuple[str]
    ) -> None:
        """
            Test that access_nested_map raises a KeyError
            for non-existent paths.
        """
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """
        Tests for the get_json function, which fetches JSON data
        from a specified URL.
    """

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    @patch("requests.get")
    def test_get_json(
        self, test_url: str, test_payload: Dict[str, Any], mock_get: Mock
    ) -> None:
        """
            Test that get_json returns the correct JSON response
            from a given URL.
        """
        mock_get.return_value.json.return_value = test_payload
        self.assertEqual(get_json(test_url), test_payload)
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """
        Tests for the memoize decorator, ensuring cached function results.
    """

    def test_memoize(self) -> None:
        """
            Test that the memoize decorator caches the result of a method.
        """

        class TestClass:
            """
                Example class to test the memoize decorator
                with a sample method and property.
            """

            def a_method(self) -> int:
                """
                    Sample method returning a constant integer.
                """
                return 42

            @memoize
            def a_property(self) -> int:
                """Property decorated with memoize to cache its result."""
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mocked:
            test_class = TestClass()
            self.assertEqual(test_class.a_property, 42)
            self.assertEqual(test_class.a_property, 42)
            mocked.assert_called_once()
