from unittest import TestCase, main

import numpy as np


def solve(m: np.ndarray) -> np.ndarray:
    return np.flipud(m.T)


# In-place with just 1 additional space unit but has poor memory access?
def solve2(m: np.ndarray) -> np.ndarray:
    for i in range(0, len(m) // 2):
        k = len(m) - i - 1
        for j in range(i, k):
            l = i - j + k
            m[i, j], m[j, k], m[k, l], m[l, i] = m[j, k], m[k, l], m[l, i], m[i, j]
    return m


class TestSolution(TestCase):
    def test(self) -> None:
        m = np.random.randn(5, 5).astype(np.float32)
        n = np.rot90(m).copy()
        np.testing.assert_array_equal(solve(m), n)

    def test2(self) -> None:
        m = np.random.randn(5, 5).astype(np.float32)
        n = np.rot90(m).copy()
        np.testing.assert_array_equal(solve2(m), n)


if __name__ == "__main__":
    main()
