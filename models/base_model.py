#!/usr/bin/python3
"""this module implements the base class module"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    this is a class base model that defines all common
    attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """this is a class construnctor method"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            setattr(self, "created_at",
                    datetime.strptime(kwargs['created_at'],
                                      "%Y-%m-%dT%H:%M:%S.%f"))
            setattr(self, "updated_at",
                    datetime.strptime(kwargs['updated_at'],
                                      "%Y-%m-%dT%H:%M:%S.%f"))
        else:
            self.id = str(uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        this method  should print: [<class name>] (<self.id>) <self.__dict__>
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """this method updates the public instance
        attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """this method  returns a dictionary containing
        all keys/values of __dict__ of the instance"""
        dictionary = self.__dict__
        dict_cpy = dictionary.copy()
        dict_cpy.update({"__class__": self.__class__.__name__, "updated_at":
                           self.updated_at.isoformat(), "created_at":
                           self.created_at.isoformat()})
        return dict_cpy
