from collections import defaultdict, deque
from random import choice, randrange, sample
from typing import Sequence
from unittest import TestCase, main

from common import time_limit


def solve(a: Sequence[str], s: str) -> int:
    ql = deque([(0, len(a))])
    qr = deque[tuple[int, int]]([])

    while ql or qr:
        if not qr:
            ql, qr = qr, ql

        offset, length = qr.popleft()
        if length == 0:
            continue

        m = length // 2
        n = offset + m
        if (t := a[n]) == s:
            return n

        if t == "":
            ql.append((offset, m))
            ql.append((n + 1, length - m - 1))
        else:
            if s < t:
                qr.clear()
                ql.append((offset, m))
            else:
                ql.clear()
                ql.append((n + 1, length - m - 1))

    raise ValueError(f"{s} is not in list")


class RandDivStr(Sequence[str]):
    def __init__(self, length: int, density: float = 0.1) -> None:
        self.length = length
        l3n = int(length * density)
        keys = sorted(sample(range(length), l3n))
        values = sorted(str(randrange(l3n)) for _ in range(l3n))
        self.dict = defaultdict(str, zip(keys, values))

    def __str__(self) -> str:
        return str([self[i] for i in range(len(self))])

    def __len__(self) -> int:
        return self.length

    def __getitem__(self, idx) -> str:
        return self.dict[idx]

    def index(self, value: str) -> int:
        for k, v in self.dict.items():
            if v == value:
                return k
        raise ValueError(f"{value} is not in list")


class TestSolution(TestCase):
    def test(self) -> None:
        density = 0.1
        it = 1_000
        for i in range(it):
            a = RandDivStr(i, density)
            s = str(randrange(int(it * density)))
            try:
                a.index(s)
            except ValueError:
                with self.assertRaises(ValueError):
                    solve(a, s)
            else:
                idx = solve(a, s)
                self.assertEqual(a[idx], s)

    def test_speed(self) -> None:
        t = 1  # much lower values than the actual time also work... why?
        n = 1_000_000
        a = RandDivStr(n)
        s = choice(list(a.dict.values()))
        with time_limit(t):
            solve(a, s)


if __name__ == "__main__":
    main()
