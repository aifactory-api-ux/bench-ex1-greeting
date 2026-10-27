import unittest

from src.greeting import greet


class TestGreeting(unittest.TestCase):
    def test_normal_name(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")

    def test_name_with_spaces(self):
        self.assertEqual(greet("  Alice  "), "Hello, Alice!")

    def test_empty_string(self):
        self.assertEqual(greet(""), "Hello, World!")
