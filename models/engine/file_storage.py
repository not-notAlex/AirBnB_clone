#!/usr/bin/python3
"""
serializes instances from a file
"""


import json
from models.base_model import BaseModel


class FileStorage:
    """
    creates and loads json files
    """
    __file_path = 'file.json'
    __objects = {}
    cls = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def all(self):
        """
        returns all objects
        """
        return self.__objects

    def new(self, obj):
        """
        creates a new object
        """
        if obj:
            o = obj.__class__.__name__ + "." + obj.id
            self.__objects.update({o: obj})

    def save(self):
        """
        saves objects to file
        """
        new_dict = {}
        for key, val in self.__objects.items():
            new_dict.update({key: val.to_dict()})
        with open(self.__file_path, 'w') as f:
            json.dump(new_dict, f)

    def reload(self):
        """
        loads objects from file
        """
        try:
            with open(self.__file_path, 'r') as f:
                old_objects = json.load(f)
            for key, val in old_objects.items():
                for k, v in val.items():
                    if v in self.cls:
                        obj = BaseModel(**val)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
