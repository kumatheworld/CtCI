from collections import UserList
from dataclasses import dataclass
from typing import Iterable, Optional

from common import T


@dataclass
class CyclicInt:
    value: int
    order: int

    def __post_init__(self) -> None:
        self.value %= self.order

    def __index__(self) -> int:
        return self.value

    def __iadd__(self, other: int) -> "CyclicInt":
        self.value = (self.value + other) % self.order
        return self

    def __add__(self, other: int) -> int:
        return (self.value + other) % self.order


class CircularArray(UserList[T]):
    def __init__(self, initlist: Optional[Iterable[T]] = None) -> None:
        self._data = list(initlist) if initlist else []
        self.base = CyclicInt(0, len(self._data))

    @property
    def data(self) -> list[T]:
        b = self.base
        return self._data[b:] + self._data[:b]

    def __setitem__(self, i: int, item: T) -> None:
        self._data[(self.base + i) % len(self)] = item

    def rotate(self, n: int) -> None:
        self.base += n
