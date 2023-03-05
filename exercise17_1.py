from itertools import zip_longest
from random import randrange
from typing import Iterator
from unittest import TestCase, main


def signed_revbins(n: int) -> tuple[bool, Iterator[bool]]:
    sign, bs = bin(n).split("0b")
    return bool(sign), (b == "1" for b in reversed(bs))


def add_bits(a: bool, b: bool, c: bool) -> tuple[bool, bool]:
    return a ^ b ^ c, (a and b) or (b and c) or (c & a)


def solve(x: int, y: int) -> int:
    sx, bx = signed_revbins(x)
    sy, by = signed_revbins(y)
    l = []
    c = False
    for a, b in zip_longest(bx, by, fillvalue=False):
        d, c = add_bits(a, b, c)
        l.append(d)
    l.append(c)
    z = int("".join("01"[e] for e in reversed(l)), 2)
    return z


class TestSolution(TestCase):
    def test(self) -> None:
        it = 1000
        n = 1000
        for _ in range(it):
            x = randrange(-n, n)
            y = randrange(-n, n)
            self.assertEqual(solve(x, y), x + y)


if __name__ == "__main__":
    main()
