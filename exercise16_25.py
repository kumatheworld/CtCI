from collections import deque
from collections.abc import Iterable, MutableMapping
from typing import Optional

from common import T, U


class DequeLRUCache(MutableMapping[T, U]):
    def __init__(
        self, iterable: Iterable[tuple[T, U]], maxlen: Optional[int] = None
    ) -> None:
        self._q = deque(iterable, maxlen)

    def __getitem__(self, __key: T) -> U:
        return super().__getitem__(__key)

    def __setitem__(self, __key: T, __value: U) -> None:
        return super().__setitem__(__key, __value)

    def __delitem__(self, __key: T) -> None:
        return super().__delitem__(__key)

    def __iter__(self):
        return iter(self._q)

    def __len__(self):
        return len(self._q)
