#!/usr/bin/python3
"""This module defines a classs file storage, for serialization and
to json for storage"""
import json


class FileStorage():
    """a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects.update({key: obj})

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        object_dict = FileStorage.__objects
        data_to_save = {}
        for obj_key, obj in object_dict.items():
            data_to_save[obj_key] = obj.to_dict()
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(data_to_save, json_file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file"""
        if FileStorage.__file_path:
            with open(FileStorage.__file_path) as json_file:
                FileStorage.__objects = json.load(json_file)
