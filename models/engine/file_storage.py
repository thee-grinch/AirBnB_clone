#!/usr/bin/python3
"""This module defines a classs file storage, for serialization and 
to json for storage"""


class FileStorage():
    """a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return cls.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        cls.__objects.update({obj.__class__.__name__ : obj})

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(cls.__file_path, "w") as json_file:
            json.dump(cls.__objects, json_file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file"""
        if cls.__file_path:
            with open(cls.__file_path) as json_file:
                cls.__objects = json.load(json_file)
