#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    def setUp(self):
        """Setup function"""
        self.console = HBNBCommand()
        self.output = StringIO

    def tearDown(self):
        """Tear down function"""
        self.output.close()

    def test_help(self):
        """Tests the do_help function"""
        with patch('sys.output', new=self.output):
            self.console.onecmd('help')
        self.assertIn("Documented commands (type help <topic>)",
                      self.output.getvalue())

    def test_help_all(self):
        """Tests the do_all function"""
        with patch('sys.output', new=self.output):
            self.console.onecmd('help all')
        self.assertIn("Print the string representation of all \
                       instances based on class name.", self.output.getvalue())

    def test_create_missing_class(self):
        """
        Tests if create without a classname gives the expected error
        """
        with patch('sys.stdout', new=self.output):
            self.console.onecmd('create')
        self.assertIn("** class name missing **", self.output.getvalue())

    def test_create_nonexistent_class(self):
        """
        Test the 'create' command with a nonexistent class name.
        """
        with patch('sys.stdout', new=self.output):
            self.console.onecmd("create MyModel")
        self.assertIn("** class doesn't exist **", self.output.getvalue())

    def test_create_base_model(self):
        """
        Test the 'create' command with the 'BaseModel' class.
        """
        with patch('sys.stdout', new=self.output):
            self.console.onecmd("create BaseModel")
            instance_id = self.output.getvalue().strip()
            self.assertIsNotNone(instance_id)

    def test_show_missing_class(self):
        """
        Test the 'show' command with a missing class name.
        """
        with patch('sys.stdout', new=self.output):
            self.console.onecmd("show")
        self.assertIn("** class name missing **", self.output.getvalue())

    def test_show_nonexistent_class(self):
        """
        Test the 'show' command with a nonexistent class name.
        """
        with patch('sys.stdout', new=self.output):
            self.console.onecmd("show MyModel")
        self.assertIn("** class doesn't exist **", self.output.getvalue())

    def test_show_missing_instance_id(self):
        """
        Test the 'show' command with a missing instance ID.
        """
        with patch('sys.stdout', new=self.output):
            self.console.onecmd("show BaseModel")
        self.assertIn("** instance id missing **", self.output.getvalue())

    def test_destroy_missing_class(self):
        """
        Test the 'destroy' command with a missing class name.
        """
        with patch('sys.stdout', new=self.output):
            self.console.onecmd("destroy")
        self.assertIn("** class name missing **", self.output.getvalue())

    def test_destroy_nonexistent_class(self):
        """
        Test the 'destroy' command with a nonexistent class name.
        """
        with patch('sys.stdout', new=self.output):
            self.console.onecmd("destroy MyModel")
        self.assertIn("** class doesn't exist **", self.output.getvalue())

    def test_destroy_missing_instance_id(self):
        """
        Test the 'destroy' command with a missing instance ID.
        """
        with patch('sys.stdout', new=self.output):
            self.console.onecmd("destroy BaseModel")
        self.assertIn("** instance id missing **", self.output.getvalue())

    def test_all_no_instances(self):
        """
        Test the 'all' command when there are no instances.
        """
        with patch('sys.stdout', new=self.output):
            self.console.onecmd("all")
        self.assertIn("No instance found", self.output.getvalue())

    def test_all_missing_class(self):
        """
        Test the 'all' command with a missing class name.
        """
        with patch('sys.stdout', new=self.output):
            self.console.onecmd("all MyModel")
        self.assertIn("** class doesn't exist **", self.output.getvalue())

    def test_update_missing_class(self):
        """
        Test the 'update' command with a missing class name.
        """
        with patch('sys.stdout', new=self.output):
            self.console.onecmd("update")
        self.assertIn("** class name missing **", self.output.getvalue())

    def test_update_nonexistent_class(self):
        """
        Test the 'update' command with a nonexistent class name.
        """
        with patch('sys.stdout', new=self.output):
            self.console.onecmd("update MyModel")
        self.assertIn("** class doesn't exist **", self.output.getvalue())


if __name__ == '__main__':
    unittest.main()
