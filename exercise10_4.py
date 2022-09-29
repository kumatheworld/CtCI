from random import choice, choices, randrange
from unittest import TestCase, main

from common import time_limit
from exercise10 import binary_search


class Listy(list[int]):
    def __getitem__(self, idx: int) -> int:
        if idx < 0:
            raise IndexError(f"negative index {idx} is not allowed")
        try:
            return super().__getitem__(idx)
        except IndexError:
            return -1

    def __repr__(self) -> str:
        return "Listy"

    def __len__(self) -> int:
        raise NotImplementedError


def solve(l: Listy, x: int) -> int:
    c = 1 << 2

    if l[c] < 0 or x < l[c]:
        return l.index(x, 0, c)

    def solve_(offset: int, length: int) -> int:
        if (m := length // 2) == 0:
            return l.index(x, offset, offset + length)

        n = offset + m
        y = l[n]
        if x < y:
            return binary_search(l, x, offset, n)
        if y < 0:
            return solve_(offset, m)
        return solve_(n, length - m)

    i = c
    j = i << 1
    while 0 < l[j] <= x:
        i = j
        j <<= 1
    return solve_(i, i)


class TestSolution(TestCase):
    def test(self) -> None:
        it = 1_000
        for i in range(it):
            a = sorted(choices(range(1, i + 1), k=i))
            l = Listy(a)
            x = randrange(i + 1)
            try:
                a.index(x)
            except ValueError:
                with self.assertRaises(ValueError):
                    solve(l, x)
            else:
                idx = solve(l, x)
                self.assertEqual(a[idx], x)

    def test_speed(self) -> None:
        t = 1  # much lower values than the actual time also work... why?
        n = 1_000_000
        a = sorted(choices(range(n), k=n))
        l = Listy(a)
        x = choice(a)
        with time_limit(t):
            solve(l, x)


if __name__ == "__main__":
    main()
