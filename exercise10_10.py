from bisect import bisect_right, insort
from collections import UserList
from random import randrange
from unittest import TestCase, main

from common import CT


class RankedSequence(UserList[CT]):
    def track(self, x: CT) -> None:
        insort(self.data, x)

    def get_rank(self, x: CT) -> int:
        idx = bisect_right(self.data, x) - 1
        if idx < 0 or self.data[idx] != x:
            raise ValueError(f"{x} is not in sequence")
        return idx


class TestSolution(TestCase):
    def test(self) -> None:
        it = 100
        size = 1000
        for _ in range(it):
            l = []
            s = RankedSequence[int]()
            for _ in range(size):
                x = randrange(size)
                y = randrange(size)
                l.append(x)
                s.track(x)
                try:
                    l.index(y)
                except ValueError:
                    with self.assertRaises(ValueError):
                        s.get_rank(y)
                else:
                    rank = sum(1 for z in l if z <= y) - 1
                    self.assertEqual(s.get_rank(y), rank)


if __name__ == "__main__":
    main()
