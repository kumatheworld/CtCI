from unittest import TestCase, main

import numpy as np

from common import CT


def solve(a: list[CT], na: int, b: list[CT]) -> None:
    ia = na - 1
    ib = len(b) - 1
    for i in range(ia + ib + 1, -1, -1):
        if ia < 0 or (ib >= 0 and a[ia] < b[ib]):
            a[i] = b[ib]
            ib -= 1
        else:
            a[i] = a[ia]
            ia -= 1


class TestSolution(TestCase):
    def test(self) -> None:
        it = 10
        for _ in range(it):
            n = 12345
            m = 6789
            a = np.random.randint(n, size=n + m + 10)
            b = np.random.randint(m, size=m)
            c = np.concatenate((a[:n], b))
            a[:n].sort()
            b.sort()
            c.sort()
            solve(a, n, b)
            np.testing.assert_array_equal(a[: n + m], c)


if __name__ == "__main__":
    main()
