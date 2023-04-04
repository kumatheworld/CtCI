from contextlib import suppress
from unittest import TestCase, main

from numpy import nonzero


def solve(l: list[int]) -> int:
    i = 1
    vol = 0
    with suppress(IndexError):
        while True:
            (above,) = nonzero([x >= i for x in l])
            vol += above[-1] - above[0] + 1
            i += 1
    return vol - sum(l)


class TestSolution(TestCase):
    def test(self) -> None:
        l = [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0]
        self.assertEqual(solve(l), 26)


if __name__ == "__main__":
    main()
