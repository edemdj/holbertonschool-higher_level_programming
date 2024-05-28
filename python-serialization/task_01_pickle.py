#!/usr/bin/env python3
import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        """initialize the object with the given attributes"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """print the object's attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """serialize the objet and save it to the specified file"""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"An error occurred while serializing: {e}")

    @classmethod
    def deserialize(cls, filename):
        """load and deserialize the object from the specified file"""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError) as e:
            print(f"An error occurred while deserializing: {e}")
            return None
