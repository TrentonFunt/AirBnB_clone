#!/usr/bin/python3
"""
This module contains the FileStorage class definition
"""
import json
from models.base_model import BaseModel
import os.path


class FileStorage:
    """
    FileStorage class definition
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump({k: v.to_dict()
                       for k, v in FileStorage.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                FileStorage.__objects = {}
                data = json.load(f)
                for k, v in data.items():
                    self.new(eval(v["__class__"])(**v))