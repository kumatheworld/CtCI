from unittest import TestCase, main

import numpy as np


# technically solve() could always return the zero matrix
def solve(m: np.ndarray) -> np.ndarray:
    return m if m.all() else np.zeros_like(m)


class TestSolution(TestCase):
    def test_pos(self) -> None:
        m = np.random.rand(3, 4)
        m[1, 2] = 0
        np.testing.assert_array_equal(solve(m), np.zeros_like(m))

    def test_neg(self) -> None:
        m = np.random.rand(3, 4) + 1
        np.testing.assert_array_equal(solve(m), m)


if __name__ == "__main__":
    main()
