from random import randrange
from unittest import TestCase, main


def solve(x: int, y: int) -> int:
    ax = abs(x)
    ay = abs(y)
    sign = (x > 0) ^ (y > 0)
    if ax < ay:
        ax, ay = ay, ax
    z = 0
    d = 1
    while ay:
        if ay & 1:
            z += ax * d
        ay >>= 1
        d <<= 1
    return -z if sign else z


class TestSolution(TestCase):
    def test(self) -> None:
        it = 1000
        a = -1000
        b = 1000
        for _ in range(it):
            x = randrange(a, b)
            y = randrange(a, b)
            self.assertEqual(solve(x, y), x * y)


if __name__ == "__main__":
    main()
