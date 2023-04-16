from data_structures.queue import Queue
import pytest

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class AnimalShelter:
    def __init__(self):
        self.dogs = []
        self.cats = []

    def enqueue(self, animal):
        if isinstance(animal, Dog):
            self.dogs.append(animal)
        elif isinstance(animal, Cat):
            self.cats.append(animal)

    def dequeue(self, preference=None):
        if preference == 'dog':
            if self.dogs:
                return self.dogs.pop(0)
        elif preference == 'cat':
            if self.cats:
                return self.cats.pop(0)
        else:  # no preference
            if self.dogs:
                return self.dogs.pop(0)
            elif self.cats:
                return self.cats.pop(0)
        print("Not a dog or cat!")
        return Animal("")  # return an instance of Animal with empty name instead of None
