#!/usr/bin/python3
"""Defines the TestStorage class"""

import os
import unittest
from unittest.mock import patch
from models.user import User
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestStorage(unittest.TestCase):
    """Defines tests for File storage functions"""
    def setUp(self):
        """Setup function"""
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.user = User()

    def tearDown(self):
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all_return_dict(self):
        """Test that 'all' returns the correct type"""
        objects = self.storage.all()
        self.assertIsInstance(objects, dict)

    def test_add_new_object(self):
        """Test that 'new' method works"""
        self.storage.new(self.base_model)
        key = f"{type(self.base_model).__name__}.{self.base_model.id}"
        self.assertIn(key, self.storage.all())

    def test_save_creates_file(self):
        with patch('builtins.open', create=True) as mock_open:
            self.storage.save()
            mock_open.assert_called_once_with(FileStorage.
                                              _FileStorage__file_path, 'w')

    def test_reload_loads_object_from_file(self):
        """Test that the reload method loads objects from Json file"""
        self.storage.new(self.user)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()

        key = f"{type(self.user).__name__}.{self.user.id}"
        self.assertIn(key, new_storage._FileStorage__objects)


if __name__ == "__main__":
    unittest.main()
