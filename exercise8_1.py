from collections import deque
from functools import cache
from unittest import TestCase, main

from common import time_limit


def solve(n: int) -> int:
    q = deque((0, 0, 1))
    for _ in range(n):
        q.append(q.popleft() + sum(q))
    return q[-1]


class TestSolution(TestCase):
    @staticmethod
    @cache
    def solve_rec(n: int) -> int:
        if n < 0:
            return 0
        if n == 0:
            return 1
        f = TestSolution.solve_rec
        return f(n - 1) + f(n - 2) + f(n - 3)

    def test(self) -> None:
        n = 100
        for _ in range(n):
            self.assertEqual(solve(n), self.solve_rec(n))

    def test_speed(self) -> None:
        n = 1000
        with time_limit(1):
            solve(n)


if __name__ == "__main__":
    main()
