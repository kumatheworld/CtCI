from random import sample
from typing import Optional
from unittest import TestCase, main


def solve(a: list[int]) -> Optional[int]:
    def solve_(offset: int, length: int) -> Optional[int]:
        if not length:
            return None

        m = length // 2
        n = offset + m
        d = a[n] - n
        if d < 0:
            return solve_(n + 1, length - m - 1)
        elif d > 0:
            return solve_(offset, m)
        else:
            return n

    return solve_(0, len(a))


class TestSolution(TestCase):
    def test(self) -> None:
        it = 1000
        l3n = 1000
        itv = range(-200, 1200)
        for _ in range(it):
            a = sorted(sample(itv, l3n))
            ids = [i for i, x in enumerate(a) if i == x]
            b = solve(a)
            if ids:
                self.assertIsNotNone(b)
                self.assertIn(b, ids)
            else:
                self.assertIsNone(b)


if __name__ == "__main__":
    main()
