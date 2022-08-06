from abc import ABC, abstractmethod
from collections.abc import Iterator, MutableSet
from dataclasses import dataclass
from itertools import chain
from typing import Generic

from common import T
from exercise2 import LinkedList


class HashFunction(ABC, Generic[T]):
    capacity: int

    @abstractmethod
    def __call__(self, element: T) -> int:
        pass


class HashTable(MutableSet[T]):
    def __init__(self, hash_fn: HashFunction) -> None:
        self._data = [LinkedList[T]() for _ in range(hash_fn.capacity)]
        self.hash_fn = hash_fn

    def __str__(self) -> str:
        return "\n".join(f"{i}: {ll}" for i, ll in enumerate(self._data) if ll)

    def __contains__(self, element: T) -> bool:
        idx = self.hash_fn(element)
        ll = self._data[idx]
        return element in ll

    def __iter__(self) -> Iterator[T]:
        return chain.from_iterable(self._data)

    def __len__(self) -> int:
        return sum(len(ll) for ll in self._data)

    def add(self, element: T) -> None:
        idx = self.hash_fn(element)
        ll = self._data[idx]
        if element not in ll:
            ll.append(element)

    def discard(self, element: T) -> None:
        idx = self.hash_fn(element)
        ll = self._data[idx]
        try:
            ll.remove(element)
        except ValueError:
            raise ValueError(f"{element} not in table") from None


@dataclass
class OrdSum(HashFunction[str]):
    capacity: int

    def __call__(self, element: str) -> int:
        return sum(ord(c) for c in element) % self.capacity
