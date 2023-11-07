#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlaceAttributes
"""
import unittest
from models.place import Place


class TestPlaceAttributes(unittest.TestCase):
    """Test cases for Place Model"""
    def setUp(self):
        self.place = Place()

    def tearDown(self):
        del self.place

    def test_has_city_id_attribute(self):
        """Test if the place object has the 'city_id' attribute."""
        self.assertTrue(hasattr(self.place, 'city_id'))

    def test_has_user_id_attribute(self):
        """Test if the place object has the 'user_id' attribute."""
        self.assertTrue(hasattr(self.place, 'user_id'))

    def test_has_name_attribute(self):
        """Test if the place object has the 'name' attribute."""
        self.assertTrue(hasattr(self.place, 'name'))

    def test_has_description_attribute(self):
        """Test if the place object has the 'description' attribute."""
        self.assertTrue(hasattr(self.place, 'description'))

    def test_has_number_rooms_attribute(self):
        """Test if the place object has the 'number_rooms' attribute."""
        self.assertTrue(hasattr(self.place, 'number_rooms'))

    def test_has_number_bathrooms_attribute(self):
        """Test if the place object has the 'number_bathrooms' attribute."""
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))

    def test_has_max_guest_attribute(self):
        """Test if the place object has the 'max_guest' attribute."""
        self.assertTrue(hasattr(self.place, 'max_guest'))

    def test_has_price_by_night_attribute(self):
        """Test if the place object has the 'price_by_night' attribute."""
        self.assertTrue(hasattr(self.place, 'price_by_night'))

    def test_has_latitude_attribute(self):
        """Test if the place object has the 'latitude' attribute."""
        self.assertTrue(hasattr(self.place, 'latitude'))

    def test_has_longitude_attribute(self):
        """Test if the place object has the 'longitude' attribute."""
        self.assertTrue(hasattr(self.place, 'longitude'))

    def test_has_amenity_ids_attribute(self):
        """Test if the place object has the 'amenity_ids' attribute."""
        self.assertTrue(hasattr(self.place, 'amenity_ids'))

    def test_city_id_default_value(self):
        """Test if the default value of city_id is an empty string."""
        self.assertEqual(self.place.city_id, '')

    def test_user_id_default_value(self):
        """Test if the default value of user_id is an empty string."""
        self.assertEqual(self.place.user_id, '')

    def test_name_default_value(self):
        """Test if the default value of name is an empty string."""
        self.assertEqual(self.place.name, '')

    def test_description_default_value(self):
        """Test if the default value of description is an empty string."""
        self.assertEqual(self.place.description, '')

    def test_number_rooms_default_value(self):
        """Test if the default value of number_rooms is 0."""
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_bathrooms_default_value(self):
        """Test if the default value of number_bathrooms is 0."""
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest_default_value(self):
        """Test if the default value of max_guest is 0."""
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night_default_value(self):
        """Test if the default value of price_by_night is 0."""
        self.assertEqual(self.place.price_by_night, 0)

    def test_latitude_default_value(self):
        """Test if the default value of latitude is 0.0."""
        self.assertEqual(self.place.latitude, 0.0)

    def test_longitude_default_value(self):
        """Test if the default value of longitude is 0.0."""
        self.assertEqual(self.place.longitude, 0.0)

    def test_amenity_ids_default_value(self):
        """Test if the default value of amenity_ids is an empty list."""
        self.assertEqual(self.place.amenity_ids, [])

    def test_city_id_assignment(self):
        """Test assigning a value to city_id attribute."""
        self.place.city_id = '12345'
        self.assertEqual(self.place.city_id, '12345')

    def test_user_id_assignment(self):
        """Test assigning a value to user_id attribute."""
        self.place.user_id = 'user123'
        self.assertEqual(self.place.user_id, 'user123')

    def test_name_assignment(self):
        """Test assigning a value to name attribute."""
        self.place.name = 'New York'
        self.assertEqual(self.place.name, 'New York')

    def test_description_assignment(self):
        """Test assigning a value to description attribute."""
        self.place.description = 'A great place to visit.'
        self.assertEqual(self.place.description, 'A great place to visit.')

    def test_number_rooms_assignment(self):
        """Test assigning a value to number_rooms attribute."""
        self.place.number_rooms = 5
        self.assertEqual(self.place.number_rooms, 5)

    def test_number_bathrooms_assignment(self):
        """Test assigning a value to number_bathrooms attribute."""
        self.place.number_bathrooms = 3
        self.assertEqual(self.place.number_bathrooms, 3)

    def test_max_guest_assignment(self):
        """Test assigning a value to max_guest attribute."""
        self.place.max_guest = 6
        self.assertEqual(self.place.max_guest, 6)

    def test_price_by_night_assignment(self):
        """Test assigning a value to price_by_night attribute."""
        self.place.price_by_night = 100
        self.assertEqual(self.place.price_by_night, 100)

    def test_latitude_assignment(self):
        """Test assigning a value to latitude attribute."""
        self.place.latitude = 40.7128
        self.assertEqual(self.place.latitude, 40.7128)

    def test_longitude_assignment(self):
        """Test assigning a value to longitude attribute."""
        self.place.longitude = -74.0060
        self.assertEqual(self.place.longitude, -74.0060)

    def test_amenity_ids_assignment(self):
        """Test assigning a list to amenity_ids attribute."""
        amenity_list = [1, 2, 3]
        self.place.amenity_ids = amenity_list
        self.assertEqual(self.place.amenity_ids, amenity_list)

    def test_city_id_type(self):
        """Test if the city_id attribute is of type str."""
        self.assertIsInstance(self.place.city_id, str)

    def test_user_id_type(self):
        """Test if the user_id attribute is of type str."""
        self.assertIsInstance(self.place.user_id, str)

    def test_name_type(self):
        """Test if the name attribute is of type str."""
        self.assertIsInstance(self.place.name, str)

    def test_description_type(self):
        """Test if the description attribute is of type str."""
        self.assertIsInstance(self.place.description, str)

    def test_number_rooms_type(self):
        """Test if the number_rooms attribute is of type int."""
        self.assertIsInstance(self.place.number_rooms, int)

    def test_number_bathrooms_type(self):
        """Test if the number_bathrooms attribute is of type int."""
        self.assertIsInstance(self.place.number_bathrooms, int)

    def test_max_guest_type(self):
        """Test if the max_guest attribute is of type int."""
        self.assertIsInstance(self.place.max_guest, int)

    def test_price_by_night_type(self):
        """Test if the price_by_night attribute is of type int."""
        self.assertIsInstance(self.place.price_by_night, int)

    def test_latitude_type(self):
        """Test if the latitude attribute is of type float."""
        self.assertIsInstance(self.place.latitude, float)

    def test_longitude_type(self):
        """Test if the longitude attribute is of type float."""
        self.assertIsInstance(self.place.longitude, float)

    def test_amenity_ids_type(self):
        """Test if the amenity_ids attribute is of type list."""
        self.assertIsInstance(self.place.amenity_ids, list)


if __name__ == '__main__':
    unittest.main()
