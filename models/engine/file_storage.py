#!/usr/bin/python3
"""Module for storage"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class FileStorage:
    """Class to serializes and deserialize JSON file
    Attributes:
        __file_path: path to the JSON file
        __objects: objects to store
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """func returns a dictionary of __object
        """
        dic = {}
        if cls:
            dictionary = self.__objects
            for key in dictionary:
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    dic[key] = self.__objects[key]
            return (dic)
        else:
            return self.__objects

    def new(self, obj):
        """sets __object to given obj
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize file path to JSON
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, val in (json.load(f)).items():
                    val = eval(va["__class__"])(**value)
                    self.__objects[key] = val
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ delete an existing element
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """ close func
        """
        self.reload()
