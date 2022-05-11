from unittest import TestCase, main

import numpy as np


# Technically solve() could always return the zero matrix
def solve(m: np.ndarray) -> None:
    cols, rows = np.nonzero(m == 0)
    m[cols] = 0
    m[:, rows] = 0


class TestSolution(TestCase):
    # Just look at the printed arrays!
    def test(self) -> None:
        m = np.random.randint(10, 100, (6, 10))
        m[m > 95] = 0
        print(m)
        solve(m)
        print(m)


if __name__ == "__main__":
    main()
