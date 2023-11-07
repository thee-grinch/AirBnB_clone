#!/usr/bin/python3
"""Defines unittests for models/review.py.

Unittest classes:
    TestReviewAttributes
"""
import unittest
from models.review import Review


class TestReviewAttributes(unittest.TestCase):
    """Test cases for Review class """

    def setUp(self):
        """Setup function"""
        self.review = Review()

    def tearDown(self):
        """Tear down function"""
        del self.review

    def test_has_place_id_attribute(self):
        """Test if the Review object has the 'place_id' attribute."""
        self.assertTrue(hasattr(self.review, 'place_id'))

    def test_has_user_id_attribute(self):
        """Test if the Review object has the 'user_id' attribute."""
        self.assertTrue(hasattr(self.review, 'user_id'))

    def test_has_text_attribute(self):
        """Test if the Review object has the 'text' attribute."""
        self.assertTrue(hasattr(self.review, 'text'))

    def test_place_id_default_value(self):
        """Test if the default value of place_id is an empty string."""
        self.assertEqual(self.review.place_id, '')

    def test_user_id_default_value(self):
        """Test if the default value of user_id is an empty string."""
        self.assertEqual(self.review.user_id, '')

    def test_text_default_value(self):
        """Test if the default value of text is an empty string."""
        self.assertEqual(self.review.text, '')

    def test_place_id_assignment(self):
        """Test assigning a value to place_id attribute."""
        self.review.place_id = '12345'
        self.assertEqual(self.review.place_id, '12345')

    def test_user_id_assignment(self):
        """Test assigning a value to user_id attribute."""
        self.review.user_id = 'user123'
        self.assertEqual(self.review.user_id, 'user123')

    def test_text_assignment(self):
        """Test assigning a value to text attribute."""
        self.review.text = 'This is a great place!'
        self.assertEqual(self.review.text, 'This is a great place!')

    def test_place_id_type(self):
        """Test if the place_id attribute is of type str."""
        self.assertIsInstance(self.review.place_id, str)

    def test_user_id_type(self):
        """Test if the user_id attribute is of type str."""
        self.assertIsInstance(self.review.user_id, str)

    def test_text_type(self):
        """Test if the text attribute is of type str."""
        self.assertIsInstance(self.review.text, str)


if __name__ == '__main__':
    unittest.main()
