#!/usr/bin/python3
"""Module"""
import json
import os.path


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            dict_list = [obj.to_dictionary() for obj in list_objs]
            json_string = cls.to_json_string(dict_list)
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of dictionaries from the JSON string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an instance with all attributes set from the dictionary"""
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy_instance = cls(1)
        else:
            raise ValueError("Unsupported class type")

        dummy_instance.update(**dictionary)
        return dummy_instance
    
    @classmethod
    def load_from_file(cls):
        """Load instances from a JSON file"""
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []  # File doesn't exist, return an empty list
        
        with open(filename, 'r') as file:
            json_string = file.read()
            dict_list = cls.from_json_string(json_string)  # Convert JSON string to list of dictionaries
            instances = [cls.create(**obj_dict) for obj_dict in dict_list]  # Create instances from dictionaries
            return instances
