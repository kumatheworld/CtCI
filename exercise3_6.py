from abc import ABCMeta
from collections import deque


class Animal(metaclass=ABCMeta):
    def __new__(cls, *args, **kwargs):
        if cls is Animal:
            raise Exception("Animal class cannot be instantiatied")
        return super(Animal, cls).__new__(cls, *args, **kwargs)


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class AnimalShelter(Animal):
    def __init__(self) -> None:
        self.qa = deque[Animal]()
        self.qd = deque[Dog]()
        self.qc = deque[Cat]()

    def __repr__(self) -> str:
        return repr([f"{type(a).__name__[0]}{(id(a) % 100)}" for a in self.qa])

    def enque(self, animal: Animal) -> None:
        self.qa.append(animal)
        if isinstance(animal, Dog):
            self.qd.append(animal)
        elif isinstance(animal, Cat):
            self.qc.append(animal)
        else:
            raise ValueError("input is neither a dog nor a cat")

    def deque_any(self) -> Animal:
        animal = self.qa.popleft()
        if isinstance(animal, Dog):
            self.qd.popleft()
        elif isinstance(animal, Cat):
            self.qc.popleft()
        return animal

    def deque_dog(self) -> Dog:
        animal = self.qd.popleft()
        self.qa.remove(animal)
        return animal

    def deque_cat(self) -> Cat:
        animal = self.qc.popleft()
        self.qa.remove(animal)
        return animal
