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
        pass


if __name__ == "__main__":
    main()
