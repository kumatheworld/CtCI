from itertools import chain, combinations, combinations_with_replacement
from unittest import TestCase, main

import numpy as np


def solve(m: np.ndarray) -> tuple[set[int], set[int]]:
    return (set(), set())


class TestSolution(TestCase):
    def test(self) -> None:
        n = 5
        it = 100
        powerset = list(
            chain.from_iterable(combinations(range(n), i) for i in range(1, n + 1))
        )
        best_sum = 0
        for _ in range(it):
            m = 2 * n * np.random.rand(n, n) - n
            for s, t in combinations_with_replacement(powerset, 2):
                if (ss := m[np.ix_(s, t)].sum()) > best_sum:
                    best_sum = ss
        u, v = solve(m)
        self.assertEqual(m[np.ix_(u, v)], best_sum)


if __name__ == "__main__":
    main()
