#!/usr/bin/python3
"""
    Module File Storage
"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage():
    """Class File Storage"""

    __file_path = 'file.json'
    __objects = dict()

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key_obj = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key_obj] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dict = {}
        for key, value in FileStorage.__objects.items():
            dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(dict, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                dict = json.load(f)
                for k, v in dict.items():
                    FileStorage.__objects[k] = eval(v['__class__'])(**v)
        except Exception:
            return
