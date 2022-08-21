from itertools import chain, combinations
from unittest import TestCase, main

from common import T


def solve(s: set[T]) -> set[frozenset[T]]:
    return set(
        chain.from_iterable(
            (frozenset(t) for t in combinations(s, n)) for n in range(len(s) + 1)
        )
    )


class TestSolution(TestCase):
    def test(self) -> None:
        s = "kumatheworld"
        for i in range(len(s) + 1):
            pref = set(s[:i])
            t = set(solve(pref))
            self.assertEqual(len(t), 1 << i)
            for u in t:
                self.assertTrue(u.issubset(pref))


if __name__ == "__main__":
    main()
