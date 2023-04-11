from itertools import chain, combinations, pairwise
from random import choices
from unittest import TestCase, main

import numpy as np


def solve(l: list[int]) -> int:
    sum_inc = 0
    sum_exc = 0
    for x in l:
        sum_inc, sum_exc = sum_exc + x, max(sum_inc, sum_exc)
    return max(sum_inc, sum_exc)


class TestSolution(TestCase):
    def test(self) -> None:
        n = 10
        it = 100
        for i in range(n):
            powerset = chain.from_iterable(
                combinations(range(i), j) for j in range(i + 1)
            )
            acceptable = [s for s in powerset if all(k - j > 1 for j, k in pairwise(s))]
            ppl = range(15, 15 * n, 15)
            for _ in range(it):
                l = choices(ppl, k=i)
                opt = 0
                for s in acceptable:
                    opt = max(opt, np.array(l)[[s]].sum())
                self.assertEqual(solve(l), opt)


if __name__ == "__main__":
    main()
