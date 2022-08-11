from functools import cache
from unittest import TestCase, main

from common import recursion_limit, time_limit

rec_lim = 1_000_000


@recursion_limit(rec_lim)
def solve(n: int) -> int:
    @cache
    def solve_(k: int) -> int:
        if k < 0:
            return 0
        if k == 0:
            return 1
        return solve_(k - 1) + solve_(k - 2) + solve_(k - 3)

    return solve_(n)


class TestSolution(TestCase):
    def test_first_couple(self) -> None:
        self.assertEqual([solve(n) for n in range(4)], [1, 1, 2, 4])

    def test_runtime(self) -> None:
        n = 1000
        with time_limit(1):
            solve(n)


if __name__ == "__main__":
    main()
