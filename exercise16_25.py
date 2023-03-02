from collections import deque
from collections.abc import Iterable, MutableMapping
from contextlib import suppress
from typing import Optional
from unittest import TestCase, main

from common import T, U


class DequeLRUCache(MutableMapping[T, U]):
    def __init__(
        self, iterable: Iterable[tuple[T, U]], maxlen: Optional[int] = None
    ) -> None:
        self._q = deque(iterable, maxlen)

    def __getitem__(self, __key: T) -> U:
        i, v = self._find(__key)
        q = self._q
        del q[i]
        q.append((__key, v))
        return v

    def __setitem__(self, __key: T, __value: U) -> None:
        with suppress(KeyError):
            del self[__key]
        self._q.append((__key, __value))

    def __delitem__(self, __key: T) -> None:
        i, _ = self._find(__key)
        del self._q[i]

    def __iter__(self):
        return iter(self._q)

    def __len__(self):
        return len(self._q)

    def _find(self, __key: T) -> tuple[int, U]:
        for i, (k, v) in enumerate(self._q):
            if k == __key:
                return i, v
        raise KeyError(__key)


class TestSolution(TestCase):
    def test(self) -> None:
        c = DequeLRUCache[str, int]([("cracking", 8)], maxlen=3)
        c["the"] = 3
        self.assertEqual(c["cracking"], 8)
        c["coding"] = 6
        c["interview"] = 9
        with self.assertRaises(KeyError):
            c["the"]
        self.assertEqual(c["cracking"], 8)


if __name__ == "__main__":
    main()
