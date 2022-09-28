from collections import Counter
from itertools import groupby
from random import choices
from typing import Iterable
from unittest import TestCase, main

from common import T, time_limit


def tci(s: Iterable[T]) -> tuple[tuple[T, int], ...]:
    return tuple(Counter(s).items())


def solve(a: list[str]) -> None:
    a.sort(key=tci)


class TestSolution(TestCase):
    def test(self) -> None:
        it = 10
        n = 10_000
        for _ in range(it):
            a = [bin(i) for i in choices(range(n), k=n)]
            b = a.copy()
            solve(a)
            self.assertEqual(sorted(a), sorted(b))
            self.assertEqual(
                len(list(groupby(tci(s) for s in a))), len(set(tci(s) for s in b))
            )

    def test_speed(self) -> None:
        t = 10
        n = 1_000_000
        a = [bin(i) for i in choices(range(n), k=n)]
        with time_limit(t):
            solve(a)


if __name__ == "__main__":
    main()
