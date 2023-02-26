from itertools import chain, combinations
from random import choices, randrange
from unittest import TestCase, main


def solve(l: list[int], s: int) -> list[list[int]]:
    return []


class TestSolution(TestCase):
    def test(self) -> None:
        it = 1000
        n = 100
        rng = range(-n, n)
        for _ in range(it):
            l = choices(rng, k=randrange(n))
            s = randrange(n)
            pairs = sorted(tuple(sorted(p)) for p in combinations(l, 2) if sum(p) == s)
            self.assertEqual(sorted(tuple(sorted(p)) for p in solve(l, s)), pairs)


if __name__ == "__main__":
    main()
