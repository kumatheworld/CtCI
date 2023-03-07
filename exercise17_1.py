from itertools import count, zip_longest
from random import randrange
from typing import Iterator
from unittest import TestCase, main


def revbins(n: int) -> tuple[bool, int, Iterator[bool]]:
    sign, bs = bin(n).split("0b")
    return bool(sign), len(bs), (b == "1" for b in reversed(bs))


def add_bits(a: bool, b: bool, c: bool) -> tuple[bool, bool]:
    return a ^ b ^ c, (a and b) or (b and c) or (c & a)


def add_pos_rev(
    bx: Iterator[bool], by: Iterator[bool], carry: bool = False
) -> Iterator[bool]:
    c = carry
    for a, b in zip_longest(bx, by, fillvalue=False):
        d, c = add_bits(a, b, c)
        yield d
    yield c


def solve(x: int, y: int) -> int:
    if abs(x) < abs(y):
        x, y = y, x
    sx, lx, bx = revbins(x)
    sy, ly, by = revbins(y)

    if sx == sy:
        bz = list(add_pos_rev(bx, by))
    else:
        bz = list(add_pos_rev(bx, (not b for b in by), carry=True))
        for i in count(ly):
            bzi = bz[i]
            bz[i] = not bzi
            if bzi:
                break

    z = int("".join("01"[e] for e in reversed(bz)), 2)

    return -z if sx else z


class TestSolution(TestCase):
    def test(self) -> None:
        it = 100000
        n = 1000
        for _ in range(it):
            x = randrange(-n, n)
            y = randrange(-n, n)
            self.assertEqual(solve(x, y), x + y)


if __name__ == "__main__":
    main()
