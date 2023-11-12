#!/usr/bin/python3
"""This module defines a classs file storage, for serialization and
to json for storage"""
import json
from datetime import datetime
import os


class FileStorage():
    """a class FileStorage that serializes instances
    to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        class_name = type(obj).__name__
        id = obj.id
        key = class_name + '.' + id
        FileStorage.__objects.update({key: obj})

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        object_to_save = {}
        for key in FileStorage.__objects:
            object_to_save[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(object_to_save, file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file"""
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.review import Review
        from models.amenity import Amenity
        from models.base_model import BaseModel

        dict_ = {
            'BaseModel': BaseModel,
            'User': User,
            'City': City,
            'Place': Place,
            'Amenity': Amenity,
            'State': State,
            'Review': Review
        }
        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path,
                  'r', encoding='utf-8') as json_file:
            content = json.load(json_file)

            FileStorage.__objects = {}
        for key, value in content.items():
            name = key.split('.')[0]
            instance = dict_[name](**value)
            if 'updated_at' in value:
                instance.updated_at = datetime.\
                                      fromisoformat(value['updated_at'])
            if 'created_at' in value:
                instance.created_at = datetime.\
                                      fromisoformat(value['created_at'])
            FileStorage.__objects[key] = instance
            FileStorage.__objects
