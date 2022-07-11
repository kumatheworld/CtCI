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
        return self._data[b:] + self._data[:b]

    def __len__(self) -> int:
        return len(self._data)

    # TODO: i: SupportsIndex | slice, item: T | Iterable[T] correnspondingly
    def __setitem__(self, i: int, item: T) -> None:
        self._data[self.base + i] = item

    # TODO: i: SupportsIndex | slice
    def __delitem__(self, i: int) -> None:
        b = self.base
        del self._data[j := (b + i) % len(self)]
        if j < b:
            self.base -= 1

    def rotate(self, n: int) -> None:
        self.base = (self.base + n) % len(self)
