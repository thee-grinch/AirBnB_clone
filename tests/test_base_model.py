import unittest
from models.base_model import BaseModel
import datetime

"""This module has all the unittests of the base_model and their methods"""

class test_init_with_kwargs(unittest.TestCase):
    """this is a class defining all the test cases of the init function"""

    def test_data_types(self):
        cls1 = BaseModel(id="b6a6e15c-c67d-4312-9a75-9d084935e579", created_at="2017-09-28T21:05:54.119427", updated_at="2017-09-28T21:05:54.119427")
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
if __name__ == '__main__':
    unittest.main()
        
