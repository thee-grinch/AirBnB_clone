#!/usr/bin/python3
"""Defines unittests for models/state.py.

Unittest classes:
    TestStateAttributes
"""
import unittest
from models.state import State


class TestStateAttributes(unittest.TestCase):
    """
        Test cases for the State class.
    """

    def test_create_state(self):
        """Test that an State instance can be created."""
        state = State()
        self.assertIsInstance(state, State)

    def test_state_has_name(self):
        """Test that an State object has a 'name' attribute."""
        state = State()
        self.assertTrue(hasattr(state, 'name'))

    def test_state_name_type(self):
        """Test that the 'name' attribute of State is of type str."""
        state = State()
        self.assertIsInstance(state.name, str)

    def test_state_name_default_value(self):
        """
            Test that the 'name' attribute of State has the
            default value of an empty string.
        """
        state = State()
        self.assertEqual(state.name, '')

    def test_state_name_assignment(self):
        """
            Test setting the 'name' attribute of State
            with a valid string value.
        """
        state = State()
        state.name = 'Arizona'
        self.assertEqual(state.name, 'Arizona')


if __name__ == '__main__':
    unittest.main()
