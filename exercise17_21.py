from contextlib import suppress
from itertools import pairwise
from random import choices
from unittest import TestCase, main

from numpy import nonzero


def solve(l: list[int]) -> int:
    if not l:
        return 0

    s = sorted(set(l))
    vol = s[0] * len(l) - sum(l)
    for h, k in pairwise(s):
        (above,) = nonzero([x >= k for x in l])
        vol += (k - h) * (above[-1] - above[0] + 1)
    return vol


class TestSolution(TestCase):
    def test(self) -> None:
        n = 100
        for i in range(n):
            l = choices(range(i), k=i)

            j = 1
            vol = -sum(l)
            with suppress(IndexError):
                while True:
                    (above,) = nonzero([x >= j for x in l])
                    vol += above[-1] - above[0] + 1
                    j += 1

            self.assertEqual(solve(l), vol)


if __name__ == "__main__":
    main()
