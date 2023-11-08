#!/usr/bin/python3
"""Defines unittests for models/city.py.

Unittest classes:
    TestUserAttributes
"""
import unittest
from models.user import User


class TestUserAttributes(unittest.TestCase):
    """ Test Cases for User Model"""

    def setUp(self):
        """ Initialize a User instance before each test"""
        self.user = User()

    def tearDown(self):
        """Clean up the User instance after each test"""
        del self.user

    def test_email_default_value(self):
        """Test that the default value of email is an empty string"""
        self.assertEqual(self.user.email, "")

    def test_password_default_value(self):
        """Test that the default value of password is an empty string"""
        self.assertEqual(self.user.password, "")

    def test_first_name_default_value(self):
        """Test that the default value of first_name is an empty string"""
        self.assertEqual(self.user.first_name, "")

    def test_last_name_default_value(self):
        """Test that the default value of last_name is an empty string"""
        self.assertEqual(self.user.last_name, "")

    def test_email_assignment(self):
        """Test assigning a value to the email attribute"""
        email_value = "test@example.com"
        self.user.email = email_value
        self.assertEqual(self.user.email, email_value)

    def test_password_assignment(self):
        """Test assigning a value to the password attribute"""
        password_value = "secure_password"
        self.user.password = password_value
        self.assertEqual(self.user.password, password_value)

    def test_first_name_assignment(self):
        """Test assigning a value to the first_name attribute"""
        first_name_value = "John"
        self.user.first_name = first_name_value
        self.assertEqual(self.user.first_name, first_name_value)

    def test_last_name_assignment(self):
        """Test assigning a value to the last_name attribute"""
        last_name_value = "Doe"
        self.user.last_name = last_name_value
        self.assertEqual(self.user.last_name, last_name_value)

    def test_email_is_string(self):
        """Test that the 'email' attribute is of type str."""
        self.assertIsInstance(self.user.email, str)

    def test_password_is_string(self):
        """Test that the 'password' attribute is of type str."""
        self.assertIsInstance(self.user.password, str)

    def test_first_name_is_string(self):
        """Test that the 'first_name' attribute is of type str."""
        self.assertIsInstance(self.user.first_name, str)

    def test_last_name_is_string(self):
        """Test that the 'last_name' attribute is of type str."""
        self.assertIsInstance(self.user.last_name, str)


if __name__ == "__main__":
    unittest.main()
