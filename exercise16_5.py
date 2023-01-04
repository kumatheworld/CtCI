import re
from math import factorial
from unittest import TestCase, main


def solve(n: int) -> int:
    return 0


class TestSolution(TestCase):
    def test(self) -> None:
        p = r"0*$"
        n = 1000
        for i in range(n):
            j = len(re.findall(p, str(factorial(i)))[0])
            self.assertEqual(solve(i), j)


if __name__ == "__main__":
    main()
