from unittest import TestCase, main

import numpy as np


def solve(l: list[int]) -> tuple[int, int]:
    # If the array is sorted, (m, n) can be any (i, i) where i < len(l)?
    x = np.array(l)
    y = np.sort(x)
    (z,) = np.nonzero(x != y)
    try:
        return z[0], z[-1]
    except IndexError:
        return 0, 0


class TestSolution(TestCase):
    def test(self) -> None:
        data = [
            ([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19], (3, 9)),
        ]
        for x, y in data:
            self.assertEqual(solve(x), y)


if __name__ == "__main__":
    main()
