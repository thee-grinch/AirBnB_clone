import unittest
from models.base_model import BaseModel
import datetime
import sys
from io import StringIO

"""This module has all the unittests of the base_model and their methods"""


class test_init_with_kwargs(unittest.TestCase):
    """this is a class defining all the test cases of the init function"""

    def test_data_types(self):
        cls1 = BaseModel(id="b6a6e15c-c67d-4312-9a75-9d084935e579",
                         created_at="2017-09-28T21:05:54.119427",
                         updated_at="2017-09-28T21:05:54.119427")
        self.assertIsInstance(cls1.id, str)
        self.assertIsInstance(cls1.created_at, datetime.datetime)
        self.assertIsInstance(cls1.updated_at, datetime.datetime)
        self.assertIsInstance(cls1, BaseModel)


class test_init_without_kwargs(unittest.TestCase):
    """This is a class method to test the init method without kwargs"""

    def test_data_types(self):
        cl1 = BaseModel()
        cl2 = BaseModel()
        self.assertIsInstance(cl1.id, str)
        self.assertIsInstance(cl1.created_at, datetime.datetime)
        self.assertIsInstance(cl1.updated_at, datetime.datetime)
        self.assertIsInstance(cl1, BaseModel)
        self.assertIsInstance(cl2.id, str)
        self.assertIsInstance(cl2.created_at, datetime.datetime)
        self.assertIsInstance(cl2.updated_at, datetime.datetime)
        self.assertIsInstance(cl2, BaseModel)

    def test_unique_id(self):
        cl1 = BaseModel()
        cl2 = BaseModel()
        self.assertNotEqual(cl1.id, cl2.id)

class test_str_method(unittest.TestCase):
    """this is a class to test the __str__ method"""
    def test_print(self):
        saved_output = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            my_class = BaseModel()
            print(my_class)
            output = out.getvalue().strip()
            self.assertEqual(output, f"[{my_class.__class__.__name__}] {my_class.id} {my_class.__dict__}")
        finally:
            sys.stdout = saved_output

class test_save_method(unittest.TestCase):
    """this method tests the save method"""
    def test_save(self):
        """this method tests the save method"""
        my_class = BaseModel()
        my_class.save()
        self.assertAlmostEqual(my_class.updated_at, datetime.datetime.now(), delta=datetime.timedelta(seconds=1))

class test_to_dict_method(unittest.TestCase):
    """this tests  the to dict method of the object"""
    def test_to_dict(self):
        my_class = BaseModel()
        my_dict = my_class.to_dict()
        self.assertIsInstance(my_dict, dict)
        self.assertIsInstance(my_dict["updated_at"], str)
        self.assertIsInstance(my_dict["created_at"], str)

if __name__ == '__main__':
    unittest.main()
