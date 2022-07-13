from collections import UserList
from typing import Iterable, Optional

from common import T


class CircularArray(UserList[T]):
    def __init__(self, initlist: Optional[Iterable[T]] = None) -> None:
        self._data = list(initlist) if initlist else []
        self.base = 0

    @property
    def data(self) -> list[T]:
        b = self.base
        self._data = self._data[b:] + self._data[:b]
        self.base = 0
        return self._data

    def __contains__(self, item: T) -> bool:
        return item in self._data

    def __len__(self) -> int:
        return len(self._data)

    # TODO: i: SupportsIndex | slice
    def __getitem__(self, i: int):
        return self._data[(self.base + i) % len(self)]

    # TODO: i: SupportsIndex | slice, item: T | Iterable[T] correnspondingly
    def __setitem__(self, i: int, item: T) -> None:
        self._data[self.base + i] = item

    def rotate(self, n: int) -> None:
        self.base = (self.base + n) % len(self)
