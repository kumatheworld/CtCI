from typing import TypeAlias
from unittest import TestCase, main

from numpy.random import randn

Point: TypeAlias = tuple[float, float]  # (x, y) in 2d space
Square: TypeAlias = tuple[Point, float]  # (center, side_length)
Line: TypeAlias = tuple[float, float, float]  # (a, b, c) where ax+by=c.


def solve(s1: Square, s2: Square) -> Line:
    (x1, y1), _ = s1
    (x2, y2), _ = s2
    a = y2 - y1
    b = x1 - x2
    if a == b == 0:
        a = 1
    c = a * x1 + b * y1
    return a, b, c


class TestSolution(TestCase):
    def setUp(self) -> None:
        n = 1000
        self.data = randn(n, 6)

    def test_concentric(self) -> None:
        for cx, cy, _, _, l1, l2 in self.data:
            s1 = ((cx, cy), l1)
            s2 = ((cx, cy), l2)
            a, b, c = solve(s1, s2)
            self.assertNotAlmostEqual(a * a + b * b + c + c, 0)
            self.assertAlmostEqual(a * cx + b * cy, c)

    def test_nonconcentric(self) -> None:
        for cx1, cy1, cx2, cy2, l1, l2 in self.data:
            s1 = ((cx1, cy1), l1)
            s2 = ((cx2, cy2), l2)
            a, b, c = solve(s1, s2)
            self.assertNotAlmostEqual(a * a + b * b + c + c, 0)
            self.assertAlmostEqual(a * cx1 + b * cy1, c)
            self.assertAlmostEqual(a * cx2 + b * cy2, c)


if __name__ == "__main__":
    main()
