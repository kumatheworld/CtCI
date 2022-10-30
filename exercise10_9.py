from contextlib import suppress
from unittest import TestCase, main

import numpy as np

from exercise10 import binary_search


def solve(a: np.ndarray, x: int) -> tuple[int, int]:
    for i, row in enumerate(a):
        with suppress(ValueError):
            return i, binary_search(row, x)
    raise ValueError(f"{x} is not in matrix")


class TestSolution(TestCase):
    def test(self) -> None:
        it = 1000
        size = 100
        for _ in range(it):
            m = np.random.randint(1, size)
            n = np.random.randint(1, size)
            high = m * n
            a = np.random.randint(high, size=(m, n))
            a.sort(0)
            a.sort(1)
            x = np.random.randint(high)
            # Now, how is the array sorted columnwise?
            if np.any(a == x):
                idx = solve(a, x)
                self.assertEqual(a[idx], x)
            else:
                with self.assertRaises(ValueError):
                    solve(a, x)


if __name__ == "__main__":
    main()
