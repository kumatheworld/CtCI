from itertools import product
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


if __name__ == "__main__":
    main()
