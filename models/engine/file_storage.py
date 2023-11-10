#!/usr/bin/python3
"""This module defines a classs file storage, for serialization and 
to json for storage"""
import json
from datetime import datetime

class FileStorage():
    """a class FileStorage that serializes instances to a JSON file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj['__class__']}.{obj['id']}"
        FileStorage.__objects.update({key : obj})

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        for dictionary in FileStorage.__objects.values():
            if isinstance(dictionary["updated_at"], datetime):
                dictionary["updated_at"] = dictionary["updated_at"].isoformat()
            if isinstance(dictionary["created_at"], datetime):
                dictionary["created_at"] = dictionary["created_at"].isoformat()
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(FileStorage.__objects, json_file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file"""
        if FileStorage.__file_path:
            try:
                with open(FileStorage.__file_path, 'r', encoding='utf-8') as json_file:
                    content = json_file.read()
                    if content:
                        File = json.loads(content)
                        FileStorage.__objects.update(File)
                for dictionary in FileStorage.__objects.values():
                    dictionary["updated_at"] = datetime.fromisoformat(dictionary["updated_at"])
                    dictionary["created_at"] = datetime.fromisoformat(dictionary["created_at"])
            except Exception as e:
                pass
