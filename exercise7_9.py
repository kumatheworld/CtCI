from collections import UserList
from typing import Iterable, Optional

from common import T


class CircularArray(UserList[T]):
    def __init__(self, initlist: Optional[Iterable[T]] = None) -> None:
        self.base = 0
        self._data = list(initlist) if initlist else []

    @property
    def data(self) -> list[T]:
        b = self.base
        return self._data[b:] + self._data[:b]

    def rotate(self, n: int) -> None:
        self.base = (self.base + n) % len(self)
