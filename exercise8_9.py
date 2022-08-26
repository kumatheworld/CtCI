from functools import cache
from typing import Iterator
from unittest import TestCase, main


def solve(n: int) -> Iterator[str]:
    return iter(())


class TestSolution(TestCase):
    @staticmethod
    def is_valid(parens: str) -> bool:
        leftness = 0
        for c in parens:
            match c:
                case "(":
                    leftness += 1
                case ")":
                    if leftness == 0:
                        return False
                    leftness -= 1
                case _:
                    return False
        return leftness == 0

    @staticmethod
    @cache
    def num_patterns(n: int) -> int:
        if n < 2:
            return 1
        f = TestSolution.num_patterns
        return 3 * f(n - 1) - f(n - 2)

    def test(self) -> None:
        n = 10
        for i in range(n):
            s = set(solve(i))
            self.assertEqual(len(s), self.num_patterns(i))
            for parens in s:
                self.assertTrue(self.is_valid(parens))


if __name__ == "__main__":
    main()
