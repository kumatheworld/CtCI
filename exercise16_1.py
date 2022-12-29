from unittest import TestCase, main

import numpy as np


def solve(x: int, y: int) -> tuple[int, int]:
    x ^= y
    y ^= x
    x ^= y
    # Technically it's wrong as it creates tuple (x, y)
    return x, y


class TestSolution(TestCase):
    def test(self) -> None:
        it = 1000
        a = np.random.randint(-it, it, (it, 2))
        b = np.asarray([solve(x, y)[::-1] for x, y in a])
        np.testing.assert_array_equal(a, b)


if __name__ == "__main__":
    main()
