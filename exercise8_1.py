from collections import deque
from unittest import TestCase, main

from common import time_limit


def solve(n: int) -> int:
    q = deque((0, 0, 1))
    for _ in range(n):
        q.append(q.popleft() + sum(q))
    return q[-1]


class TestSolution(TestCase):
    def test_first_couple(self) -> None:
        self.assertEqual([solve(n) for n in range(4)], [1, 1, 2, 4])

    def test_speed(self) -> None:
        n = 1000
        with time_limit(1):
            solve(n)


if __name__ == "__main__":
    main()
