from random import choice, choices, randrange
from unittest import TestCase, main

from common import time_limit
from exercise10 import binary_search


def solve(a: list[int], x: int) -> int:
    def solve_(offset: int, length: int) -> int:
        if (m := length // 2) == 0:
            return a.index(x, offset, offset + length)

        l = a[offset]
        n = offset + m
        r = a[n]

        if x == r:
            return n

        if l <= r:
            if l <= x < r:
                return binary_search(a, x, offset, n)
            else:
                return solve_(n + 1, length - m - 1)
        else:
            if r < x < l:
                return binary_search(a, x, n + 1, offset + length)
            else:
                return solve_(offset, m)

    return solve_(0, len(a))


class TestSolution(TestCase):
    def test(self) -> None:
        it = 1_000
        for i in range(it):
            a = sorted(choices(range(i), k=i))
            shift = randrange(-1, i)
            x = randrange(-1, i)
            a = a[shift:] + a[:shift]
            try:
                a.index(x)
            except ValueError:
                with self.assertRaises(ValueError):
                    solve(a, x)
            else:
                idx = solve(a, x)
                self.assertEqual(a[idx], x)

    def test_speed(self) -> None:
        t = 1  # much lower values than the actual time also work... why?
        n = 1_000_000
        a = sorted(choices(range(n), k=n))
        shift = randrange(n)
        x = choice(a)
        a = a[shift:] + a[:shift]
        with time_limit(t):
            solve(a, x)


if __name__ == "__main__":
    main()
