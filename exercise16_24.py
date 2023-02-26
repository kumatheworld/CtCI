from bisect import bisect_left, bisect_right
from itertools import combinations
from random import choices, randrange
from unittest import TestCase, main


def solve(l: list[int], s: int) -> list[tuple[int]]:
    a = sorted(l)
    pairs = []
    j = len(a)
    for i, x in enumerate(a, 1):
        y = s - x
        j = bisect_right(a, y, i, j)
        if j < i:
            break
        m = j - bisect_left(a, y, i, j)
        pairs.extend([(x, y)] * m)
    return pairs


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
