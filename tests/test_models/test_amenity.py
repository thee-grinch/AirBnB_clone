#!/usr/bin/python3
"""Defines unittests for models/amenity.py.

Unittest classes:
    TestAmenityAttributes
"""
import unittest
from models.amenity import Amenity


class TestAmenityAttributes(unittest.TestCase):
    """
        Test cases for the Amenity class.
    """

    def test_create_amenity(self):
        """Test that an Amenity instance can be created."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_amenity_has_name(self):
        """Test that an Amenity object has a 'name' attribute."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))

    def test_amenity_name_type(self):
        """Test that the 'name' attribute of Amenity is of type str."""
        amenity = Amenity()
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)

    def test_amenity_name_default_value(self):
        """
            Test that the 'name' attribute of Amenity has the
            default value of an empty string.
        """
        amenity = Amenity()
        self.assertEqual(amenity.name, '')

    def test_amenity_name_assignment(self):
        """
            Test setting the 'name' attribute of Amenity
            with a valid string value.
        """
        amenity = Amenity()
        amenity.name = 'Swimming Pool'
        self.assertEqual(amenity.name, 'Swimming Pool')


if __name__ == '__main__':
    unittest.main()
