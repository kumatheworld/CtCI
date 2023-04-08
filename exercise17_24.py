from itertools import chain, combinations, combinations_with_replacement, product
from unittest import TestCase, main

import numpy as np


def solve(m: np.ndarray) -> tuple[set[int], set[int]]:
    return ([], [])


class TestSolution(TestCase):
    def test(self) -> None:
        n = 5
        it = 1
        powerset = list(
            chain.from_iterable(combinations(range(n), i) for i in range(1, n + 1))
        )
        print(powerset)
        best_submatrix = set(), set()
        best_sum = 0
        for _ in range(it):
            m = 2 * n * np.random.rand(n, n) - n
            print(m)
            for s, t in combinations_with_replacement(powerset, 2):
                print(s, t)
                if m[s, t].sum() > best_sum:
                    best_submatrix = s, t
        print(best_submatrix)


if __name__ == "__main__":
    main()
