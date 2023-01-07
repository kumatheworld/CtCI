from itertools import chain
from math import inf
from random import randrange
from typing import Optional
from unittest import TestCase, main

import numpy as np


def solve(l: list[int], m: list[int]) -> Optional[tuple[int, int]]:
    if not (l and m):
        return None

    lm = sorted(chain(((x, 0) for x in l), ((y, 1) for y in m)))
    a = np.asarray(lm)
    b = a[1:] - a[:-1]
    c = np.ma.masked_where(b[:, 1] == 0, b[:, 0])
    i = c.argmin()
    x = lm[i][0]
    y = lm[i + 1][0]
    return (x, y) if b[i, 1] > 0 else (y, x)


class TestSolution(TestCase):
    def test(self) -> None:
        max_size = 1000
        it = 100
        for _ in range(it):
            k = np.random.randint(
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
