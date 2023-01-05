import re
from math import factorial
from unittest import TestCase, main


def solve(n: int) -> int:
    z = 0
    w = n // 5
    while w:
        z += w
        w //= 5
    return z


class TestSolution(TestCase):
    def test(self) -> None:
        p = re.compile(r"0*$")
        n = 1000
        for i in range(n):
            m = p.search(str(factorial(i)))
            j = len(m.group())
            self.assertEqual(solve(i), j)


if __name__ == "__main__":
    main()
