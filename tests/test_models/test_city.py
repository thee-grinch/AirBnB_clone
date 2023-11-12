#!/usr/bin/python3
"""Defines unittests for models/city.py.

Unittest classes:
    TestCityAttributes
"""
import unittest
from models.city import City


class TestCityAttributes(unittest.TestCase):
    """
        Test cases for the city class.
    """

    def test_create_city(self):
        """Test that an city instance can be created."""
        city = City()
        self.assertIsInstance(city, City)

    def test_city_has_state_id(self):
        """Test that City has 'state_id' attribute"""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))

    def test_city_state_id_type(self):
        """Test that the 'state_id' attribute of City is of type str."""
        city = City()
        self.assertIsInstance(city.state_id, str)

    def test_city_state_id_default_value(self):
        """
            Test that the 'state_id' attribute of city has the
            default value of an empty string.
        """
        city = City()
        self.assertEqual(city.state_id, '')

    def test_city_state_id_assignment(self):
        """
            Test setting the 'state_id' attribute of City
            with a valid string value.
        """
        city = City()
        city.state_id = '1'
        self.assertEqual(city.state_id, '1')

    def test_city_has_name(self):
        """Test that an City object has a 'name' attribute."""
        city = City()
        self.assertTrue(hasattr(city, 'name'))

    def test_city_name_type(self):
        """Test that the 'name' attribute of City is of type str."""
        city = City()
        self.assertIsInstance(city.name, str)

    def test_city_name_default_value(self):
        """
            Test that the 'name' attribute of city has the
            default value of an empty string.
        """
        city = City()
        self.assertEqual(city.name, '')

    def test_city_name_assignment(self):
        """
            Test setting the 'name' attribute of City
            with a valid string value.
        """
        city = City()
        city.name = 'New York City'
        self.assertEqual(city.name, 'New York City')

    # def test_city_name_assignment_type_check(self):
    #     """
    #         Test that setting the 'name' attribute of City with
    #         a non-string value raises a TypeError.
    #     """
    #     city = City()
    #     with self.assertRaises(TypeError):
    #         city.name = ['some_name']


if __name__ == '__main__':
    unittest.main()
