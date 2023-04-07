from functools import partial
from itertools import product
from random import randrange
from typing import Optional, TypeAlias
from unittest import TestCase, main

import numpy as np

Point: TypeAlias = tuple[int, int]


def solve(m: np.ndarray) -> Optional[tuple[Point, Point]]:
    return None


class TestSolution(TestCase):
    def test_none(self) -> None:
        n = 5
        for i, j in product(range(n), range(n)):
            a = np.zeros((i, j), dtype=bool)
            self.assertEqual(solve(a), None)

    def test(self) -> None:
        n = 10
        it = 1000
        randbool = partial(np.random.choice, a=[False, True], p=[0.5, 0.5])
        for _ in range(it):
            i = randrange(1, n)
            j = randrange(1, n)
            m = randbool(size=(i, j))
            y = randrange(i)
            x = randrange(j)
            m[y, x] = True

            area_max = 1
            for y1, x1 in product(range(i), range(j)):
                for y0, x0 in product(range(y1 + 1), range(x1 + 1)):
                    if m[y0, x0] and m[y0, x1] and m[y1, x0] and m[y1, x1]:
                        area_max = max(area_max, (x1 - x0 + 1) * (y1 - y0 + 1))

            s = solve(m)
            self.assertIsNotNone(s)
            (i0, j0), (i1, j1) = s
            self.assertTrue(m[i0, j0] and m[i0, j1] and m[i1, j0] and m[i1, j1])
            self.assertEqual((j1 - j0 + 1) * (i1 - i0 + 1), area_max)


if __name__ == "__main__":
    main()
