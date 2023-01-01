from typing import Optional, TypeAlias
from unittest import TestCase, main

import numpy as np

Point: TypeAlias = tuple[float, float]
LinSeg: TypeAlias = tuple[Point, Point]


def solve(l: LinSeg, m: LinSeg) -> Optional[Point]:
    (xl1, yl1), (xl2, yl2) = l
    (xm1, ym1), (xm2, ym2) = m
    a = np.array(((yl2 - yl1, xl1 - xl2), (ym2 - ym1, xm1 - xm2)))
    b = np.array((xl1 * yl2 - xl2 * yl1, xm1 * ym2 - xm2 * ym1))
    try:
        p = np.linalg.solve(a, b)
    except np.linalg.LinAlgError:
        p = None
    else:
        x = p[0]
        if (
            x < min(xl1, xl2)
            or max(xl1, xl2) < x
            or x < min(xm1, xm2)
            or max(xm1, xm2) < x
        ):
            p = None
    finally:
        return p


class TestSolution(TestCase):
    def test(self) -> None:
        data = [
            # 3x - y = 1, x + 2y = 5
            ((((3, 8), (-2, -7)), ((-1, 3), (7, -1))), np.array((1.0, 2.0))),
            ((((-2, -7), (3, 8)), ((-1, 3), (7, -1))), np.array((1.0, 2.0))),
            ((((3, 8), (-2, -7)), ((7, -1), (-1, 3))), np.array((1.0, 2.0))),
            ((((-2, -7), (3, 8)), ((7, -1), (-1, 3))), np.array((1.0, 2.0))),
            ((((8, 3), (-7, -2)), ((3, -1), (-1, 7))), np.array((2.0, 1.0))),
            ((((-3, -8), (2, 7)), ((1, -3), (-7, 1))), np.array((-1.0, -2.0))),
            ((((-3, 8), (2, -7)), ((1, 3), (-7, -1))), np.array((-1.0, 2.0))),
            ((((3, -8), (-2, 7)), ((-1, -3), (7, 1))), np.array((1.0, -2.0))),
            ((((3, 8), (-2, -7)), ((3, 1), (7, -1))), None),
            ((((-2, -7), (3, 8)), ((3, 1), (7, -1))), None),
            ((((3, 8), (-2, -7)), ((7, -1), (3, 1))), None),
            ((((-2, -7), (3, 8)), ((7, -1), (3, 1))), None),
            ((((8, 3), (-7, -2)), ((1, 3), (-1, 7))), None),
            ((((-3, -8), (2, 7)), ((-3, -1), (-7, 1))), None),
            ((((-3, 8), (2, -7)), ((-3, 1), (-7, -1))), None),
            ((((3, -8), (-2, 7)), ((3, -1), (7, 1))), None),
            ((((3, 8), (-2, -7)), ((3, 8), (-2, -7))), None),
            # x = 2, y = 1
            ((((2, -1), (2, 2)), ((-1, 1), (3, 1))), np.array((2.0, 1.0))),
        ]
        for (l, m), p in data:
            if p is None:
                self.assertIsNone(solve(l, m))
            else:
                np.testing.assert_equal(solve(l, m), p)


if __name__ == "__main__":
    main()
