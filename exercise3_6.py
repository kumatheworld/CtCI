from abc import ABCMeta
from collections import deque
from operator import itemgetter


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
        self.qd = deque[tuple[int, Dog]]()
        self.qc = deque[tuple[int, Cat]]()
        self.count = 0

    def __str__(self) -> str:
        # This should be O(N) but don't care
        return str(
            [
                f"{type(a[1]).__name__[0]}{(id(a) % 100)}"
                for a in sorted(self.qd + self.qc, key=itemgetter(0))
            ]
        )

    def enque(self, animal: Animal) -> None:
        if isinstance(animal, Dog):
            self.qd.append((self.count, animal))
        elif isinstance(animal, Cat):
            self.qc.append((self.count, animal))
        else:
            raise ValueError("input is neither a dog nor a cat")
        self.count += 1

    def deque_any(self) -> Animal:
        if not self.qd:
            return self.qc.popleft()[1]
        if not self.qc:
            return self.qd.popleft()[1]
        dog = self.qd[0]
        cat = self.qc[0]
        if dog[0] < cat[0]:
            self.qd.popleft()
            return dog[1]
        else:
            self.qc.popleft()
            return cat[1]

    def deque_dog(self) -> Dog:
        return self.qd.popleft()[1]

    def deque_cat(self) -> Cat:
        return self.qc.popleft()[1]
