#!/usr/bin/env python3
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses."""
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"
