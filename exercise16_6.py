from math import inf
from random import randrange
from unittest import TestCase, main

from numpy.random import randint


def solve(l: list[int], m: list[int]) -> int:
    return 0


class TestSolution(TestCase):
    def test(self) -> None:
        max_size = 1000
        it = 100
        for _ in range(it):
            k = randint(
                -randrange(max_size), randrange(max_size), randrange(max_size) + 1
            )
            n = randrange(len(k))
            l = k[:n].tolist()
            m = k[n:].tolist()

            dmin = inf
            pairs = []
            for i in sorted(l):
                for j in sorted(m):
                    if (d := abs(i - j)) < dmin:
                        dmin = d
                        pairs = [(i, j)]
                    elif d == dmin:
                        pairs.append((i, j))

            if pairs:
                self.assertIn(solve(l, m), pairs)
            else:
                self.assertIsNone(solve(l, m))


if __name__ == "__main__":
    main()
